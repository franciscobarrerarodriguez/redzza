from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


from categories.models import Category
from django.http import HttpResponse


def test(request):
    colores(44, '#58ACFA')
    colores(155, '#3ADF00')
    colores(163, '#0101DF')
    colores(50, '#FF8000')
    colores(39, '#9e9e9e')
    colores(49, '#000000')
    colores(151, '#F5ECCE')
    colores(48, '#ff4081')
    colores(40, '#ffd600')
    colores(186, '#795548')
    colores(53, '#8e24aa')
    colores(194, '#f44336')
    return HttpResponse("finished test")


def colores(categoryPattern, color):
    categories = Category.objects.filter(pattern=categoryPattern)
    for category in categories:
        category.color = color
        category.save()
    pattern = Category.objects.get(pk=categoryPattern)
    pattern.color = color
    pattern.save()
