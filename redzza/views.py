from django.shortcuts import render
# Create your views here.
from categories.models import WantedCategory, Category
from profiles.models import Profile, Place
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Vista del index de la aplicacion, sin sesion


def index(request):
    return render(request, 'landing.html')


def queries(request):
    # get_object_or_404(Profile, gender='F')
    # query = Profile.updateBirthdate(get_object_or_404(Profile, gender='F'), "2015-11-06")
    # query = Profile.updateGender(get_object_or_404(Profile, gender='F'), 'M')
    # tunja -> 3
    query = Profile.updateLocation(get_object_or_404(Profile, gender='F'), Place.searchCity(3))
    return HttpResponse(query)
