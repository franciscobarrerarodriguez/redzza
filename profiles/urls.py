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
# from registration.backends.default.views import RegistrationView
from django.contrib.auth import views as auth_views
# from .forms import UserCreationEmailForm


urlpatterns = [
    url(r'accounts/register/(?P<step>[\w\-\W]+)/', views.singup, name='register'),
    url(r'^accounts/login/', views.loginEmail, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/home/', views.home, name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # Url para la verificacion de la existencia correo electronico al momento de registrarse
    # True --> Existe el correo, NO se puede usar
    # False --> No existe el correo, se puede usar
    url(r'^ajax/validateEmail/$', views.validateEmail, name='validateEmail'),
    # Url para la verificacion de la existencia correo electronico al momento de registrarse
    # True --> Existe el correo, NO se puede usar
    # False --> No existe el correo, se puede usar
    url(r'^ajax/validateUsername/$', views.validateUsername, name='validateUsername'),

    #URL para comprobar el funcionamiento de las consultas a la base de datos
    url(r'^accounts/queries/', views.queries, name='query')
]
