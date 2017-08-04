from django.conf.urls import url, include
from .views import ProfileViewSet, UserViewSet, PlaceViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'places', PlaceViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
