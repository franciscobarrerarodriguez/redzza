from rest_framework import viewsets
from .models import Tag, TagProfile
from .serializers import TagSerializer, TagProfileSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagProfileViewSet(viewsets.ModelViewSet):
    queryset = TagProfile.objects.all()
    serializer_class = TagProfileSerializer
