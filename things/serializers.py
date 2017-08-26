from rest_framework import serializers
from .models import Notice, CityNotice, Product, Color, Service, Image, Video, Commentary


class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'url', 'date', 'profile', 'category', 'title', 'description', 'money', 'offer', 'kind', 'visibility', 'urgency')


class CityNoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityNotice
        fields = ('id', 'url', 'city', 'notice')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'url', 'notice', 'state', 'delivery')


class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'url', 'hexa', 'product')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'url', 'notice', 'time')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'url', 'notice', 'image')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'url', 'notice', 'video')


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('id', 'url', 'notice', 'profile', 'commentary')
