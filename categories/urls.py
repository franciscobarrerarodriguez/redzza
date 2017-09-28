from rest_framework import routers
from .views import CategoryViewSet, WantedCategoryViewSet, SuggestedCategoryViewSet


router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
# router.register(r'wantedCategories', WantedCategoryViewSet)
# router.register(r'suggestedCategories', SuggestedCategoryViewSet)
