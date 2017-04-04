from django.shortcuts import render

# Create your views here.
from profiles import forms


def index(request):
    return render(request, 'landing.html', {'form': forms.EmailAuthenticationForm})
