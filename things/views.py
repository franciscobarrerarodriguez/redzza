from rest_framework import viewsets
from .models import Notice, CityNotice, Product, Color, Service, Image, Video, Commentary
from .serializers import NoticeSerializer, CityNoticeSerializer, ProductSerializer, ColorSerializer, ServiceSerializer, ImageSerializer, VideoSerializer, CommentarySerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class CityNoticeViewSet(viewsets.ModelViewSet):
    queryset = CityNotice.objects.all()
    serializer_class = CityNoticeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer
