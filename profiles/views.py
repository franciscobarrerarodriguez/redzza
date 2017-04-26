from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Profile, Place
from .forms import EmailAuthenticationForm
from categories import Category, WantedCategory
# Create your views here.


# Vista de login por correo electronico y contraseña
def loginEmail(request):
    form = EmailAuthenticationForm(request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        if form.get_user().is_staff:
            return JsonResponse({'success': True, 'url': '/admin/'})
        else:
            return JsonResponse({'success': True, 'url': '/home/'})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})


# Vista home, con sesion
@login_required
def home(request):
    return render(request, 'home.html')


# Vista perfil personal, con sesion
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


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


# Vista de obtencion de lugares
def getPlaces(request):
    data = Place.objects.all()
    data_serialized = serializers.serialize('json', data)
    return JsonResponse(data_serialized, safe=False)


# Vista para la creacion de un usuario
def createUser(request):
    email = request.POST.get('email', None)
    username = request.POST.get('name', None)
    name = request.POST.get('name', None)
    last_name = request.POST.get('last_name', None)
    password = request.POST.get('password', None)
    place = request.POST.get('place', None)
    i_search = request.POST.get('i_search', None)
    i_have = request.POST.get('i_have', None)

    if email and username and name and last_name and password and place and i_search and i_have:
        user, created = User.objects.get_or_create(
            email=email,
            username=username,
            first_name=name,
            last_name=last_name
        )
        if created:
            user.set_password(password)
            user.save()
            place = get_object_or_404(Place, id=2)
            profile = Profile(user=user, gender='F', location=place)
            profile.save()

            # recorrer objeto de categorias y crear categoria
            category = get_object_or_404(Category, id=11)
            # i_have(Ofrezco) --> 1 ; i_search(Busco) --> 2
            wanted = WantedCategory(profile=profile, category=category, type_category=1)
            wanted.save()
            login(request, user)
            return JsonResponse({'success': True, 'url': '/dashboard/'})
        else:
            return JsonResponse({'success': False, 'err': 'User not created'})
    else:
        return JsonResponse({'success': False, 'err': 'Incomplete data'})
