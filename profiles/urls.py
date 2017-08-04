from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'followers', FollowViewSet)
