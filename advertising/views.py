from rest_framework import viewsets
from .models import Advertising
from .serializers import AdvertisingSerializer


class AdvertisingViewSet(viewsets.ModelViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
