from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route, detail_route
from rest_framework.authtoken.models import Token
from allauth.account import app_settings as allauth_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import complete_signup
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from categories.models import WantedCategory, SuggestedCategory
from tags.models import TagProfile
from .models import Profile, Place, Follow
from .serializers import ProfileSerializer, UserSerializer, PlaceSerializer, FollowSerializer
from rest_framework_expiring_authtoken.models import ExpiringToken
from django.core import serializers
from redzza.settings import MEDIA_URL
from redzza.site import S3
import json
from redzza import utils


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False).order_by('date_joined').reverse()
    serializer_class = UserSerializer
    http_method_names = ['get', 'head']

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Obtencion de informacion de un usuario
    @detail_route(methods=['get'])
    def getData(self, request, pk=None):
        try:
            user = utils.getUser(pk)
            context = {}
            context['user'] = json.loads(serializers.serialize('json', [user], fields=('username', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined')))
            profile = utils.getProfile(user)
            context['profile'] = json.loads(serializers.serialize('json', [profile]))
            context['profile'][0]['fields']['location'] = utils.getDataCities([profile.location])
            context['profile'][0]['fields']['avatar'] = S3 + MEDIA_URL + str(profile.avatar)
            context['duration'] = utils.getDurationUser(user)
            context['numberFollowers'] = utils.getNumberFollowersUser(user)
            haveCategories = utils.getHaveCategoriesUser(user)
            context['haveCategories'] = json.loads(serializers.serialize('json', haveCategories))
            for i, category in enumerate(context['haveCategories']):
                context['haveCategories'][i]['fields']['name'] = str(haveCategories[i])
            searchCategories = utils.getSearchCategoriesUser(user)
            context['searchCategories'] = json.loads(serializers.serialize('json', searchCategories))
            for i, category in enumerate(context['searchCategories']):
                context['searchCategories'][i]['fields']['name'] = str(searchCategories[i])
            context['tags'] = json.loads(serializers.serialize('json', utils.getTagsUser(user)))
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Obtencion de publicacion de un usuario
    # id - imagen - titulo - kind
    @detail_route(methods=['get'])
    def getNotices(self, request, pk=None):
        try:
            user = utils.getUser(pk)
            notices = utils.getNoticesUser(user)
            context = utils.getDataNotice(notices)
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.filter(pattern=None).order_by('name')
    serializer_class = PlaceSerializer
    permission_classes = [AllowAny]

    # Obtencion de ciudades de un departamento
    @detail_route(methods=['get'])
    def getCities(self, request, pk=None):
        try:
            cities = Place.searchTowns(pk)
            context = utils.getDataCities(cities)
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class ApiServicesViewSet(viewsets.ViewSet):

    # Validacion del correo que se intenta registrar
    @list_route(methods=['post'], permission_classes=[AllowAny])
    def validateEmail(self, request):
        try:
            email = request.data.get('email', None)
            if email:
                return Response({'success': True, 'exists': Profile.searchEmail(email), 'data': email})
            else:
                return Response({'success': False, 'err': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Creacion de un usuario
    @list_route(methods=['post'], permission_classes=[AllowAny])
    def createUser(self, request):
        try:
            email = request.data.get('email', None)
            username = utils.generateRandomUsername(request.data.get('first_name', None))
            first_name = request.data.get('first_name', None)
            last_name = request.data.get('last_name', None)
            password = request.data.get('password', None)
            place = request.data.get('place', None)
            i_search = request.data.get('i_search', None)
            i_have = request.data.get('i_have', None)
            suggesting = request.data.get('suggesting', None)

            if email and username and first_name and last_name and password and place and len(i_search) > 0 and len(i_have) > 0:
                if Profile.searchEmail(email) is False:
                    if utils.validateStructureEmail(email):
                        user, created = Profile.createUser(email, username, first_name, last_name, password)
                        if created:
                            profile = Profile.create(place, user)
                            # i_have(Ofrezco) --> 1 ; i_search(Busco) --> 2
                            for element in i_have:
                                WantedCategory.create(element['pk'], profile, 1)
                            for element in i_search:
                                WantedCategory.create(element['pk'], profile, 2)
                            if suggesting:
                                SuggestedCategory.create(suggesting, profile)
                            login(request, user)
                            token = Token.objects.create(user=user)
                            userSerialized = json.loads(serializers.serialize('json', [user], fields=('username', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined')))
                            complete_signup(request._request, user, allauth_settings.EMAIL_VERIFICATION, None)
                            userSerialized[0]['fields']['is_verified'] = EmailAddress.objects.get(user=user).verified
                            return Response({'success': True, 'msg': 'user-created', 'token': token.key, 'user': userSerialized}, status=status.HTTP_201_CREATED)
                        else:
                            return Response({'success': False, 'err': 'User not created'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                    else:
                        return Response({'success': False, 'err': 'Invalid Email'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                else:
                    return Response({'success': False, 'err': 'email-exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                return Response({'success': False, 'err': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Login por correo electronico o usuario y contraseña
    @list_route(methods=['post'], permission_classes=[AllowAny])
    def loginUser(self, request):
        try:
            user = request.data.get('user', None)
            password = request.data.get('password', None)
            if utils.validateStructureEmail(user):
                userEmail = utils.getUserEmail(user)
                if userEmail is not None:
                    user = userEmail.username
            userAuthenticate = authenticate(request, username=user, password=password)
            if userAuthenticate is not None:
                login(request, userAuthenticate)
                token = utils.getToken(userAuthenticate)
                timeToken = utils.getTimeToken(token)
                userSerialized = json.loads(serializers.serialize('json', [userAuthenticate], fields=('username', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined')))
                userSerialized[0]['fields']['is_verified'] = EmailAddress.objects.get(user=userAuthenticate).verified
                if userAuthenticate.is_staff:
                    return Response({'success': True, 'msg': 'user-admin', 'user': userSerialized, 'token': token.key, 'timeToken': timeToken})
                else:
                    return Response({'success': True, 'msg': 'user-normal', 'user': userSerialized, 'token': token.key, 'timeToken': timeToken})
            else:
                return Response({'success': False, 'err': 'invalid-login'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Edicion de informacion del usuario
    @list_route(methods=['put'])
    def updateUser(self, request):
        try:
            user = request.user
            profile = utils.getProfile(user)
            username = request.data.get('username', None)
            first_name = request.data.get('first_name', None)
            last_name = request.data.get('last_name', None)
            email = request.data.get('email', None)
            avatar = request.data.get('avatar', None)
            icono = request.data.get('icono', None)
            birth_date = request.data.get('birth_date', None)
            gender = request.data.get('gender', None)
            phone = request.data.get('phone', None)
            biography = request.data.get('biography', None)
            location = request.data.get('location', None)
            company = request.data.get('company', None)
            profession = request.data.get('profession', None)
            address = request.data.get('address', None)
            avialability = request.data.get('avialability', None)
            i_search = request.data.get('i_search', None)
            i_have = request.data.get('i_have', None)
            tags = request.data.get('tags', None)

            if first_name and last_name:
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return Response({'success': True, 'msg': 'full_name-update'})
            elif username:
                if Profile.searchUsername(username) is False:
                    user.username = username
                    user.save()
                    return Response({'success': True, 'msg': 'username-update'})
                else:
                    return Response({'success': False, 'err': 'username-exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif first_name:
                user.first_name = first_name
                user.save()
                return Response({'success': True, 'msg': 'first_name-update'})
            elif last_name:
                user.last_name = last_name
                user.save()
                return Response({'success': True, 'msg': 'last_name-update'})
            elif email:
                if Profile.searchEmail(email) is False:
                    if utils.validateStructureEmail(email) is True:
                        user.email = email
                        user.save()
                        return Response({'success': True, 'msg': 'email-update'})
                    else:
                        return Response({'success': False, 'err': 'email-invalid'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'success': False, 'err': 'email-exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif avatar:
                Profile.updateAvatar(profile, avatar)
                return Response({'success': True, 'msg': 'avatar-update'})
            elif icono:
                Profile.updateIcono(profile, icono)
                return Response({'success': True, 'msg': 'icono-update'})
            elif birth_date:
                Profile.updateBirthdate(profile, birth_date)
                return Response({'success': True, 'msg': 'birth_date-update'})
            elif gender:
                Profile.updateGender(profile, gender)
                return Response({'success': True, 'msg': 'gender-update'})
            elif phone:
                Profile.updatePhone(profile, phone)
                return Response({'success': True, 'msg': 'phone-update'})
            elif biography:
                Profile.updateBiography(profile, biography)
                return Response({'success': True, 'msg': 'biography-update'})
            elif location:
                Profile.updateLocation(profile, location)
                return Response({'success': True, 'msg': 'location-update'})
            elif company:
                Profile.updateCompany(profile, company)
                return Response({'success': True, 'msg': 'company-update'})
            elif profession:
                Profile.updateProfession(profile, profession)
                return Response({'success': True, 'msg': 'profession-update'})
            elif address:
                Profile.updateAddress(profile, address)
                return Response({'success': True, 'msg': 'address-update'})
            elif avialability:
                Profile.updateAvialability(profile, avialability)
                return Response({'success': True, 'msg': 'avialability-update'})
            elif i_search:
                WantedCategory.deleteAllSearch(profile)
                for element in i_search:
                    WantedCategory.create(element['pk'], profile, 2)
                return Response({'success': True, 'msg': 'i_search-update'})
            elif i_have:
                WantedCategory.deleteAllHave(profile)
                for element in i_have:
                    WantedCategory.create(element['pk'], profile, 1)
                return Response({'success': True, 'msg': 'i_have-update'})
            elif tags:
                TagProfile.deleteAll(profile)
                for element in tags:
                    TagProfile.create(element['pk'], profile)
                return Response({'success': True, 'msg': 'tags-update'})
            else:
                return Response({'success': False, 'err': 'field-undefined'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Obtencion de home de un usuario
    @list_route(methods=['get'])
    def getHome(self, request):
        try:
            user = request.user
            profile = utils.getProfile(user)
            queries = utils.Notice.searchHome(profile.id)
            notices = utils.noticesQuery(queries)
            context = utils.getDataNotice(notices)
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # CheckTokent
    @list_route(methods=['post'], permission_classes=[AllowAny])
    def checkToken(self, request):
        try:
            key = request.data.get('token', None)
            if key is None:
                return Response({'success': False, 'err': 'field-undefined'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                token = ExpiringToken.objects.get(key=key)
            except ExpiringToken.DoesNotExist:
                return Response({'detail': 'Invalid token'})

            if not token.user.is_active:
                return Response({'detail': 'User inactive or deleted'})

            if token.expired():
                return Response({'detail': 'Token has expired'})

            return Response({'detail': 'Token has valid'})

        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
