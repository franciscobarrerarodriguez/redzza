from rest_framework import viewsets
from .models import Category, WantedCategory, SuggestedCategory
from .serializers import CategorySerializer, WantedCategorySerializer, SuggestedCategorySerializer
from rest_framework.permissions import AllowAny


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class WantedCategoryViewSet(viewsets.ModelViewSet):
    queryset = WantedCategory.objects.all()
    serializer_class = WantedCategorySerializer


class SuggestedCategoryViewSet(viewsets.ModelViewSet):
    queryset = SuggestedCategory.objects.all()
    serializer_class = SuggestedCategorySerializer
