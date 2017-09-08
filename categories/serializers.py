from rest_framework import serializers
from .models import Category, WantedCategory, SuggestedCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'pattern', 'name', 'description')


class WantedCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WantedCategory
        fields = ('id', 'url', 'category', 'profile', 'type_category')


class SuggestedCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuggestedCategory
        fields = ('id', 'url', 'category', 'profile')
