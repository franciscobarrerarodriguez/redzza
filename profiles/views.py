from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmailAuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def loginEmail(request):
    form = EmailAuthenticationForm(request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        if form.get_user().is_staff:
            return redirect('/admin/')
        else:
            return redirect('home')

    return render(request, 'registration/login.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')
