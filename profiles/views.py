from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route, detail_route
from rest_framework.authtoken.models import Token
from allauth.account import app_settings as allauth_settings
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from allauth.account.utils import complete_signup
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from categories.models import WantedCategory
from tags.models import TagProfile
from .models import Profile, Place, Follow
from .serializers import ProfileSerializer, UserSerializer, PlaceSerializer, FollowSerializer
from rest_framework_expiring_authtoken.models import ExpiringToken
from django.core import serializers
from redzza.settings import MEDIA_URL
from redzza.site import S3
import json
from redzza import utils
from django.core.cache import cache


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False).order_by('date_joined').reverse()
    serializer_class = UserSerializer
    http_method_names = ['get', 'head']

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
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
    http_method_names = ['post', 'head']

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        follower = utils.getProfile(request.user)
        user = request.data.get('user', None)

        if user is None:
            return Response({'success': False, 'err': 'field-undefined'}, status=status.HTTP_400_BAD_REQUEST)

        following = utils.getProfile(utils.getUser(user))
        if Follow.checkFollowing(follower.id, following.id):
            return Response({'success': False, 'err': 'already following'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        request.data['following'] = following.id
        request.data['follower'] = follower.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        utils.sendEmail(following.user.email, 'notifications/new_follower.html')
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
            created = False
            email = request.data.get('email', None)
            username = utils.generateRandomUsername(request.data.get('first_name', None))
            first_name = request.data.get('first_name', None)
            last_name = request.data.get('last_name', None)
            password = request.data.get('password', None)

            if email and username and first_name and last_name and password:
                if Profile.searchEmail(email) is False:
                    if utils.validateStructureEmail(email):
                        user, created = Profile.createUser(email, username, first_name, last_name, password)
                        if created:
                            idPlace = Place.searchName("Sin definir").id
                            Profile.create(idPlace, user)
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
            if created:
                user.delete()
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Login por correo electronico o usuario y contraseña
    @list_route(methods=['post'], permission_classes=[AllowAny])
    def loginUser(self, request):
        try:
            user = request.data.get('user', None)
            password = request.data.get('password', None)
            if utils.validateStructureEmail(user):
                userEmail = utils.getUserEmailNoSocial(user)
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
                if utils.validateStructureEmail(user):
                    checkUser = utils.getUserEmail(user)
                else:
                    checkUser = utils.getUserUsername(user)
                socialaccount = SocialAccount.objects.filter(user=checkUser)
                if socialaccount is not None:
                    for account in socialaccount:
                        if account.provider == 'facebook':
                            return Response({'success': False, 'err': 'f'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                        if account.provider == 'google':
                            return Response({'success': False, 'err': 'g'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                return Response({'success': False, 'err': 'l'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
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

            response = {'success': False, 'err': 'field-undefined'}

            if username:
                if Profile.searchUsername(username) is False:
                    user.username = username
                    user.save()
                    response = {'success': True, 'msg': 'username-update'}
                else:
                    response = {'success': False, 'err': 'username-exists'}
            if first_name:
                user.first_name = first_name
                user.save()
                response = {'success': True, 'msg': 'first_name-update'}
            if last_name:
                user.last_name = last_name
                user.save()
                response = {'success': True, 'msg': 'last_name-update'}
            if email:
                if Profile.searchEmail(email) is False:
                    if utils.validateStructureEmail(email) is True:
                        EmailAddress.change(EmailAddress.objects.get(user=user), request, email)
                        response = {'success': True, 'msg': 'email-update'}
                    else:
                        response = {'success': False, 'err': 'email-invalid'}
                else:
                    response = {'success': False, 'err': 'email-exists'}
            if avatar:
                Profile.updateAvatar(profile, avatar)
                response = {'success': True, 'msg': 'avatar-update'}
            if icono:
                Profile.updateIcono(profile, icono)
                response = {'success': True, 'msg': 'icono-update'}
            if birth_date:
                Profile.updateBirthdate(profile, birth_date)
                response = {'success': True, 'msg': 'birth_date-update'}
            if gender:
                Profile.updateGender(profile, gender)
                response = {'success': True, 'msg': 'gender-update'}
            if phone:
                Profile.updatePhone(profile, phone)
                response = {'success': True, 'msg': 'phone-update'}
            if biography:
                Profile.updateBiography(profile, biography)
                response = {'success': True, 'msg': 'biography-update'}
            if location:
                Profile.updateLocation(profile, location)
                response = {'success': True, 'msg': 'location-update'}
            if company:
                Profile.updateCompany(profile, company)
                response = {'success': True, 'msg': 'company-update'}
            if profession:
                Profile.updateProfession(profile, profession)
                response = {'success': True, 'msg': 'profession-update'}
            if address:
                Profile.updateAddress(profile, address)
                response = {'success': True, 'msg': 'address-update'}
            if avialability:
                Profile.updateAvialability(profile, avialability)
                response = {'success': True, 'msg': 'avialability-update'}
            if i_search:
                WantedCategory.deleteAllSearch(profile)
                for element in i_search:
                    WantedCategory.create(element['pk'], profile, 2)
                response = {'success': True, 'msg': 'i_search-update'}
            if i_have:
                WantedCategory.deleteAllHave(profile)
                for element in i_have:
                    WantedCategory.create(element['pk'], profile, 1)
                response = {'success': True, 'msg': 'i_have-update'}
            if tags:
                TagProfile.deleteAll(profile)
                for element in tags:
                    TagProfile.create(element['pk'], profile)
                response = {'success': True, 'msg': 'tags-update'}

            if response["success"]:
                return Response(response)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

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
            context = cache.get('home_%s' % profile.id)
            if context is None:
                queries = utils.Notice.searchHome(profile.id)
                notices = utils.noticesQuery(queries)
                context = utils.getDataNotice(notices)
                cache.set('home_%s' % profile.id, context)

            page = utils.getPagination(context, request, 20)
            if isinstance(page, str):
                return Response({'success': False, 'err': page}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif page.has_next():
                return Response({'success': True, 'data': page.object_list, 'next': page.next_page_number()})
            else:
                return Response({'success': True, 'data': page.object_list})
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

    # Verificacion de seguimiento de usuario
    @list_route(methods=['post'])
    def checkFollowing(self, request):
        try:
            following = utils.getProfile(utils.getUser(request.data.get('user', None)))
            follower = utils.getProfile(request.user)
            if following is None:
                return Response({'success': False, 'err': 'field-undefined'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': True, 'following': Follow.checkFollowing(follower, following)})

        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @list_route(methods=['post'])
    def unfollow(self, request):
        try:
            follower = utils.getProfile(request.user)

            user = request.data.get('user', None)
            if user is None:
                return Response({'success': False, 'err': 'field-undefined'}, status=status.HTTP_400_BAD_REQUEST)

            following = utils.getProfile(utils.getUser(user))

            instance = Follow.getFollowing(follower, following)
            instance.delete()
            return Response({'success': True})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
