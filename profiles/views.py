from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import *
from .serializers import *


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().filter(is_staff=False)
    serializer_class = UserSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class ApiServices(viewsets.ViewSet):

    @list_route(methods=['post'])
    def validateEmail(self, request):
        email = request.POST.get('email', None)
        if email:
            return Response({'exists': Profile.searchEmail(email), 'data': email})
        else:
            return Response({'err': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'])
    def createUser(request):
        email = request.POST.get('email', None)
        username = generate_random_username(request.POST.get('first_name', None))
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        password = request.POST.get('password', None)
        place = request.POST.get('place', None)
        i_search = request.POST.get('i_search', None)
        i_have = request.POST.get('i_have', None)
        suggesting = request.POST.get('suggesting', None)

        if email and username and first_name and last_name and password and place and i_search and i_have:
            if Profile.searchEmail(email) is False:
                if validateStructureEmail(email):
                    user, created = Profile.createUser(email, username, first_name, last_name, password)
                    if created:
                        profile = Profile.create(place, user)
                        # i_have(Ofrezco) --> 1 ; i_search(Busco) --> 2
                        for element in json.loads(i_have):
                            WantedCategory.create(element['pk'], profile, 1)
                        for element in json.loads(i_search):
                            WantedCategory.create(element['pk'], profile, 2)
                        if suggesting:
                            SuggestedCategory.create(suggesting, profile)
                        login(request, user, 'profiles.backends.EmailBackend')
                        token = Token.objects.create(user=user)
                        return Response({'success': True, 'msg': 'user-created', 'token': token}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'success': False, 'err': 'User not created'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'success': False, 'err': 'Invalid Email'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'success': False, 'err': 'email-exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'err': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)
