from rest_framework import serializers
from .models import Notice, CityNotice, Product, Color, Service, Image, Video, Commentary


class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class CityNoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityNotice
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class CommentarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commentary
        fields = '__all__'
