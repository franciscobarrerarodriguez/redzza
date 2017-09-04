from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet, ApiServicesViewSet


router = routers.SimpleRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'apiServices', ApiServicesViewSet, base_name='apiServices')
