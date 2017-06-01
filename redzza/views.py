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
    # get_object_or_404(Category, gender="Femenino")
    query = WantedCategory.searchOffer(get_object_or_404(Profile, gender='F'))
    return HttpResponse(query)
