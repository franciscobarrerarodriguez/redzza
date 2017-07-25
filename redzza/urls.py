from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from . import views
from . import settings


urlpatterns = [
    # URL para comprobar el funcionamiento de las consultas a la base de datos
    url(r'^queries/', views.queries, name='query'),
    # Url - Administracion
    url(r'^admin/', admin.site.urls, name='admin'),
    # Url - index de la aplicacion, sin sesion
    url(r'^$', views.index, name='index'),
    # Urls - referente a categorias
    url(r'^', include('categories.urls')),
    # Urls - referente a cosas
    url(r'^', include('things.urls')),
    # Urls - referente a usuarios y sus perfiles
    # ---- Debe estar de ultimas - url de usuario -----
    url(r'^', include('profiles.urls')),
    # staticfiles
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
