from rest_framework import routers
from .views import NoticeViewSet, CityNoticeViewSet, ProductViewSet, ColorViewSet, ServiceViewSet, ImageViewSet, VideoViewSet, CommentaryViewSet, ApiServicesViewSet


router = routers.DefaultRouter()
router.register(r'notices', NoticeViewSet)
router.register(r'citiesNotice', CityNoticeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'images', ImageViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'comments', CommentaryViewSet)
router.register(r'apiServices', ApiServicesViewSet, base_name='apiServices')
