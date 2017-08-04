from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Url - Administracion
    url(r'^admin/', admin.site.urls,),
    # Urls - referente a usuarios y sus perfiles
    url(r'^api/v1/', include('profiles.urls')),
    # Urls - referente a categorias
    url(r'^api/v1/', include('categories.urls')),
    # Urls - referente a cosas
    url(r'^api/v1/', include('things.urls')),
    # rest_framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
