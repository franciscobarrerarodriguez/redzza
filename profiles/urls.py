from django.conf.urls import url, include
from rest_framework import routers
from .views import ProfileViewSet, UserViewSet, PlaceViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'followers', FollowViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
