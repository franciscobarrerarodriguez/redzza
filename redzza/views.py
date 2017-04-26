from django.shortcuts import render
# Create your views here.


# Vista del index de la aplicacion, sin sesion
def index(request):
    return render(request, 'landing.html')
