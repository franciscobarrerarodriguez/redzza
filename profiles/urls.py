from rest_framework import routers
from .views import ProfileViewSet, UserViewSet, PlaceViewSet, FollowViewSet, ApiServicesViewSet


router = routers.DefaultRouter()
# router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'places', PlaceViewSet)
# router.register(r'followers', FollowViewSet)
router.register(r'apiServices', ApiServicesViewSet, base_name='apiServices')
