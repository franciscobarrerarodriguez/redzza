from rest_framework import serializers
from .models import Tag, TagProfile


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'url', 'name')


class TagProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TagProfile
        fields = ('id', 'url', 'tag', 'profile')
