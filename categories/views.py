from rest_framework import viewsets
from .models import Category, WantedCategory, SuggestedCategory
from .serializers import CategorySerializer, WantedCategorySerializer, SuggestedCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class WantedCategoryViewSet(viewsets.ModelViewSet):
    queryset = WantedCategory.objects.all()
    serializer_class = WantedCategorySerializer


class SuggestedCategoryViewSet(viewsets.ModelViewSet):
    queryset = SuggestedCategory.objects.all()
    serializer_class = SuggestedCategorySerializer
