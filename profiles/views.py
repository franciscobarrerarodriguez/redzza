from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile
# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
