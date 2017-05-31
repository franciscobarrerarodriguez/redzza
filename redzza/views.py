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
    city = Category.getSubCategories(get_object_or_404(Category, id=50))
    return HttpResponse(city)
