from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.views.static import serve
from . import settings
from . import views as vprueba

from profiles.urls import router as profiles_router
from categories.urls import router as categories_router
from things.urls import router as things_router
from tags.urls import router as tags_router
from advertising.urls import router as advertising_router
from rest_framework_expiring_authtoken import views

router = routers.DefaultRouter()
router.registry.extend(profiles_router.registry)
router.registry.extend(categories_router.registry)
router.registry.extend(things_router.registry)
router.registry.extend(tags_router.registry)
router.registry.extend(advertising_router.registry)

urlpatterns = [
    url(r'^', admin.site.urls,),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/login/', views.obtain_expiring_auth_token),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^queries/', vprueba.queries, name='query'),
]
