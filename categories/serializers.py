from rest_framework import serializers
from .models import Category, WantedCategory, SuggestedCategory
from redzza.site import S3
from redzza.settings import MEDIA_URL


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        image = serializers.SerializerMethodField()

        def get_image(self, obj):
            return S3 + MEDIA_URL + str(obj.image)

        model = Category
        fields = ('id', 'pattern', 'name', 'description', 'image', 'color')


class WantedCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WantedCategory
        fields = ('id', 'url', 'category', 'profile')


class SuggestedCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuggestedCategory
        fields = ('id', 'url', 'category', 'profile')
