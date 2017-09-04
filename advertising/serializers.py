from rest_framework import serializers
from .models import Advertising


class AdvertisingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertising
        fields = ('id', 'url', 'title', 'image')
