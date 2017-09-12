from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Place, Follow


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'url', 'user', 'avatar', 'icono', 'birth_date', 'gender', 'phone', 'biography', 'location', 'company', 'profession', 'address', 'avialability')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'pattern')


class FollowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'url', 'following', 'follower')
