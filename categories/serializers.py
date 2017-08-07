from rest_framework import serializers
from .models import Category, WantedCategory, SuggestedCategory


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'pattern', 'name', 'description')


class WantedCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WantedCategory
        fields = ('id', 'url', 'category', 'profile', 'type_category')


class SuggestedCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuggestedCategory
        fields = ('id', 'url', 'category', 'profile', 'type_category')
