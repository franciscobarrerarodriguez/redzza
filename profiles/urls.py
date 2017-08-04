from django.conf.urls import url, include
from .views import ProfileViewSet, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
