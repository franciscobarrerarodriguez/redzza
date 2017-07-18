from django.conf.urls import url
from . import views


urlpatterns = [
    # Retorna todas las categorias
    url(r'^ajax/categories/$', views.getCategories, name='getCategories'),
]
