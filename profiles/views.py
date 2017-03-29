from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmailAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.


# Vista de login por correo electronico
def loginEmail(request):
    form = EmailAuthenticationForm(request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        if form.get_user().is_staff:
            return redirect('/admin/')
        else:
            return redirect('home')

    return render(request, 'registration/login.html', {'form': form})


# Vista de redireccion al home despues de login
@login_required
def home(request):
    return render(request, 'home.html')


# Vista para el registro en fases, la fase se recibe por parametro de la url
# Paso 1 --> completar perfil
# Paso 2 --> que busco categorias
# Paso 3 --> que tengo categorias
def singup(request, step):
    return {
        'step1': render(request, 'registration/registration_1.html'),
        'step2': render(request, 'registration/registration_2.html'),
        'step3': render(request, 'registration/registration_3.html'),
    }.get(step, redirect('index'))


# Vista para la validacion del correo que se intenta registrar
# True --> Existe el correo, NO se puede usar
# False --> No existe el correo, se puede usar
def validateEmail(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


# Vista para la validacion del usuario que se intenta registrar
# True --> Existe el usuario, NO se puede usar
# False --> No existe el usuario, se puede usar
def validateUsername(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
