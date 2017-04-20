"""redzza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'register/(?P<step>[\w\-\W]+)/', views.singup, name='register'),
    url(r'^login/', views.loginEmail, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^home/', views.home, name='home'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^', include('registration.backends.default.urls')),
    # Url para la verificacion de la existencia correo electronico al momento de registrarse
    # True --> Existe el correo, NO se puede usar
    # False --> No existe el correo, se puede usar
    url(r'^ajax/validateEmail/$', views.validateEmail, name='validateEmail'),
    # Url para la verificacion de la existencia correo electronico al momento de registrarse
    # True --> Existe el correo, NO se puede usar
    # False --> No existe el correo, se puede usar
    url(r'^ajax/validateUsername/$', views.validateUsername, name='validateUsername'),

    # Retorna todas las categorias
    url(r'^ajax/categories/$', views.getCategories, name='getCategories'),

    # Retorna todos los lugares
    url(r'^ajax/places/$', views.getPlaces, name='getPlaces'),

    # Url creacion de un nuevo usuario
    url(r'^createUser/', views.createUser, name='createUser'),

    # URL para comprobar el funcionamiento de las consultas a la base de datos
    url(r'^queries/', views.queries, name='query')
]
