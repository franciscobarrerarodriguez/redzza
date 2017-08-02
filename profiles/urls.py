# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # Url para el registro en fases, la fase se recibe por parametro de la url, registro para facebook
    url(r'^register/(?P<userFacebook>[\w\-\W]+)/(?P<step>[\w\-\W]+)/', views.register, name='register_facebook'),
    # Url para el registro en fases, la fase se recibe por parametro de la url
    url(r'^register/(?P<step>[\w\-\W]+)/', views.register, name='register'),
    # Url home con sesion
    url(r'^home/', views.home, name='home'),
    # Url dashboard con sesion
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    # Url configuracion del perfil
    url(r'^settings/', views.settings, name='settings'),
    # Url - cerrar sesion
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    # Url - verificacion de la existencia correo electronico al momento de registrarse
    url(r'^ajax/validateEmail/$', views.validateEmail, name='validateEmail'),
    # Url - creacion de un nuevo usuario
    url(r'^ajax/createUser/', views.createUser, name='createUser'),
    # Url - inicio de sesion a la aplicacion, se realiza mediante correo y contraseña
    url(r'^ajax/login/', views.loginEmail, name='login'),
    # Url - Actualiza datos de usuario
    url(r'^ajax/updateUser/$', views.updateUser, name='updateUser'),
    # Url - visitar perfil
    url(r'^(?P<slug>[-_\w]+)/$', login_required(views.UserDetailView.as_view()), name='userDetail'),
    # Urls - Adicionales de registro e inicio de sesion - siempre deben estar al final
    url(r'^', include('registration.backends.default.urls')),
]
