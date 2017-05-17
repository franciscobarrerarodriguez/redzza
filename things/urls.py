from django.conf.urls import url
from . import views

urlpatterns = [
    # Url carga de html para formulario de nueva publicacion de post
    url(r'^post/', views.newPost, name='post'),
    # Url Formulario de publicacion de una cosa
    url(r'^ajax/newPost/$', views.newPost, name='newPost'),
]
