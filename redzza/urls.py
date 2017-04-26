from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    # Url - index de la aplicacion, sin sesion
    url(r'^$', views.index, name='index'),
    # Urls - referente a usuarios y sus perfiles
    url(r'^', include('profiles.urls')),
    # Urls - referente a categorias
    url(r'^', include('categories.urls')),
    # Urls - Autenticacion con red social facebook
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    # Url - Administracion
    url(r'^admin/', admin.site.urls),
]
