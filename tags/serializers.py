from rest_framework import serializers
from .models import *


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TagProfile
        fields = '__all__'
