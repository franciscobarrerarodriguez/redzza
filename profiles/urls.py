# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    # rest_framework
    url(r'^', include(router.urls)),
]
