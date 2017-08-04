from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'wantedCategories', WantedCategoryViewSet)
router.register(r'suggestedCategories', SuggestedCategoryViewSet)
