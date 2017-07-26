# -*- coding: utf-8 -*-

from random import choice
from string import ascii_lowercase, digits
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile, Place, Follow
from .forms import EmailAuthenticationForm
from django.shortcuts import get_object_or_404
import json
from categories.models import WantedCategory, SuggestedCategory, Category
from things.models import Notice
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone
# Create your views here.


# ---------------------------------VISTAS RENDER----------------------------------------

# URL --> REGISTER
# Vista para el registro en fases, la fase se recibe por parametro de la url
# Paso 1 --> completar perfil
# Paso 2 --> que busco categorias
# Paso 3 --> que tengo categorias
def register(request, step):
    user = request.user
    context = {}
    context['categories'] = getCategoriesMacro(user)
    context['places'] = getCities(user)
    return {
        'step1': render(request, 'registration/registration_1.html', context),
        'step2': render(request, 'registration/registration_2.html', context),
        'step3': render(request, 'registration/registration_3.html', context),
    }.get(step, redirect('index'))


# URL --> HOME
# Vista home, con sesion
@login_required
def home(request):
    user = request.user
    context = {}
    context['profile'] = get_object_or_404(Profile, user=user)
    return render(request, 'home.html', context)


# URL --> DASHBOARD
# Vista perfil personal, con sesion
@login_required
def dashboard(request):
    user = request.user
    context = {}
    context['profile'] = get_object_or_404(Profile, user=user)
    context['duration'] = getDurationUser(user)
    context['numberFollowers'] = getNumberFollowersUser(user)
    context['haveCategories'] = getHaveCategoriesUser(user)
    context['searchCategories'] = getSearchCategoriesUser(user)
    context['noticesHave'] = getNoticesUser(user, 1)
    context['noticesSearch'] = getNoticesUser(user, 2)
    print('FALTA MOSTRAR ETIQUETAS')
    return render(request, 'dashboard.html', context)


# URL --> SETTINGS
# Vista, configuracion del perfil
@login_required
def settings(request):
    user = request.user
    context = {}
    context['profile'] = get_object_or_404(Profile, user=user)
    return render(request, 'settings.html', context)


# ---------------------------------VISTAS AJAX----------------------------------------

# URL --> AJAX/VALIDATEEMAIL
# Vista para la validacion del correo que se intenta registrar
# True --> Existe el correo, NO se puede usar
# False --> No existe el correo, se puede usar
def validateEmail(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Profile.searchEmail(email)
    }
    return JsonResponse(data)


# URL --> AJAX/CREATEUSER
# Vista para la creacion de un usuario
def createUser(request):
    email = request.POST.get('email', None)
    username = generate_random_username(request.POST.get('name', None))
    first_name = request.POST.get('name', None)
    last_name = request.POST.get('last_name', None)
    password = request.POST.get('password', None)
    place = request.POST.get('place', None)
    i_search = request.POST.get('i_search', None)
    i_have = request.POST.get('i_have', None)
    suggesting = request.POST.get('suggesting', None)

    if email and username and first_name and last_name and password and place and i_search and i_have:
        if Profile.searchEmail(email) is False:
            if validateStructureEmail(email):
                user, created = Profile.createUser(email, username, first_name, last_name, password)
                if created:
                    profile = Profile.create(place, user)
                    # i_have(Ofrezco) --> 1 ; i_search(Busco) --> 2
                    for element in json.loads(i_have):
                        WantedCategory.create(element['pk'], profile, 1)
                    for element in json.loads(i_search):
                        WantedCategory.create(element['pk'], profile, 2)
                    if suggesting:
                        SuggestedCategory.create(suggesting, profile)
                    login(request, user)
                    return JsonResponse({'success': True, 'url': '/dashboard/'})
                else:
                    return JsonResponse({'success': False, 'msg': 'User not created'})
            else:
                return JsonResponse({'success': False, 'msg': 'Invalid Email'})
        else:
            return JsonResponse({'success': False, 'msg': 'email-exists'})
    else:
        return JsonResponse({'success': False, 'msg': 'Incomplete data'})


# URL --> LOGIN
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


# URL --> AJAX/UPDATEUSER
# Vista de modificacion de informacion del usuario
def updateUser(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    username = request.POST.get('username', None)
    name = request.POST.get('name', None)
    last_name = request.POST.get('last_name', None)
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    avatar = request.POST.get('avatar', None)
    icono = request.POST.get('icono', None)
    birth_date = request.POST.get('birth_date', None)
    gender = request.POST.get('gender', None)
    phone = request.POST.get('phone', None)
    biography = request.POST.get('biography', None)
    location = request.POST.get('location', None)
    company = request.POST.get('company', None)
    profession = request.POST.get('profession', None)
    address = request.POST.get('address', None)
    avialability = request.POST.get('avialability', None)
    i_search = request.POST.get('i_search', None)
    i_have = request.POST.get('i_have', None)
    print('FALTA RECIBIR Y UPDATE ETIQUETAS')

    if username:
        if Profile.searchUsername(username) is False:
            user.username = username
            user.save()
            return JsonResponse({'success': True, 'msg': 'username-update'})
        else:
            return JsonResponse({'success': False, 'msg': 'username-exists'})
    elif name:
        user.first_name = name
        user.save()
        return JsonResponse({'success': True, 'msg': 'name-update'})
    elif last_name:
        user.last_name = last_name
        user.save()
        return JsonResponse({'success': True, 'msg': 'last_name-update'})
    elif email:
        if Profile.searchEmail(email) is False:
            if validateEmail(email) is True:
                user.email = email
                user.save()
                return JsonResponse({'success': True, 'msg': 'email-update'})
            else:
                return JsonResponse({'success': False, 'msg': 'email-invalid'})
        else:
            return JsonResponse({'success': False, 'msg': 'email-exists'})
    elif password:
        user.set_password(password)
        user.save()
        return JsonResponse({'success': True, 'msg': 'password-update'})
    elif avatar:
        print('FALTA UPDATE DE AVATAR')
        return JsonResponse({'success': True, 'msg': 'avatar-update'})
    elif icono:
        print('FALTA UPDATE DE ICONO')
        return JsonResponse({'success': True, 'msg': 'icono-update'})
    elif birth_date:
        Profile.updateBirthdate(profile, birth_date)
        return JsonResponse({'success': True, 'msg': 'birth_date-update'})
    elif gender:
        Profile.updateGender(profile, gender)
        return JsonResponse({'success': True, 'msg': 'gender-update'})
    elif phone:
        Profile.updatePhone(profile, phone)
        return JsonResponse({'success': True, 'msg': 'phone-update'})
    elif biography:
        Profile.updateBiography(profile, biography)
        return JsonResponse({'success': True, 'msg': 'biography-update'})
    elif location:
        place = Place.searchCity(location)
        Profile.updateLocation(profile, place)
        return JsonResponse({'success': True, 'msg': 'location-update'})
    elif company:
        Profile.updateComany(profile, company)
        return JsonResponse({'success': True, 'msg': 'company-update'})
    elif profession:
        Profile.updateProfession(profile, profession)
        return JsonResponse({'success': True, 'msg': 'profession-update'})
    elif address:
        Profile.updateAddress(profile, address)
        return JsonResponse({'success': True, 'msg': 'address-update'})
    elif avialability:
        Profile.updateAvialability(profile, avialability)
        return JsonResponse({'success': True, 'msg': 'avialability-update'})
    elif i_search:
        print('FALTA UPDATE DE CATEGORIAS')
        return JsonResponse({'success': True, 'msg': 'i_search-update'})
    elif i_have:
        print('FALTA UPDATE DE CATEGORIAS')
        return JsonResponse({'success': True, 'msg': 'i_have-update'})
    else:
        return JsonResponse({'success': False, 'msg': 'nothing-update'})


# ---------------------------------METODOS LOGICOS----------------------------------------

# Metodo de verificacion de estructura del email
def validateStructureEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


# Metodo para la generacion del username unico para un nuevo usuario
def generate_random_username(name, length=8, chars=ascii_lowercase + digits, split=4, delimiter='-'):
    username = ''.join([choice(chars) for i in range(length)])
    if split:
        username = delimiter.join([username[start:start + split] for start in range(0, len(username), split)])
    username = name + '-' + username
    try:
        User.objects.get(username=username)
        return Profile.generate_random_username(name=name, length=length, chars=chars, split=split, delimiter=delimiter)
    except User.DoesNotExist:
        return username


# Metodo de creacion de perfil a partir del datos de facebook
def saveProfileFacebook(backend, user, response, *args, **kwargs):
    if len(Profile.search(user)) == 0:
        profile = Profile.create(6, user)
        if response['gender'] == 'male':
            Profile.updateGender(profile, 'M')
        else:
            Profile.updateGender(profile, 'F')
        print('FALTA UPDATE DE AVATAR')


# ---------------------------------METODOS OBTENCION DE DATOS---------------------------------

# Metodo que retorna todas las categorias macro
def getCategoriesMacro(user):
    return Category.getCategories()


# Metodo que retorna todas las categorias macro
def getCities(user):
    return Place.getCities()


# Metodo que retorna el tiempo inscrito en redzza del usuario ingresado por parametro
# Tiempo en dias
def getDurationUser(user):
    return (datetime.now(timezone.utc) - user.date_joined).days


# Metodo que retorna el numero de seguidores del usuario ingresado por parametro
def getNumberFollowersUser(user):
    return len(Follow.searchFollowers(get_object_or_404(Profile, user=user)))


# Metodo que retorna las categorias que ofrece el usuario ingresado por parametro
# i_have(Ofrezco) --> 1
def getHaveCategoriesUser(user):
    return WantedCategory.searchHave(get_object_or_404(Profile, user=user))


# Metodo que retorna las categorias que busca el usuario ingresado por parametro
# i_search(Busco) --> 2
def getSearchCategoriesUser(user):
    return WantedCategory.searchOffer(get_object_or_404(Profile, user=user))


# Metodo que retorna las publicaciones del usuario ingresado por parametro
def getNoticesUser(user, kind):
    return Notice.getNotice(get_object_or_404(Profile, user=user), kind)


# Vista basada en clase generica, retorna en contexto los datos de usuario solicitado por url
# www.redzza.com/[username]
class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'user.html'
    slug_field = 'username'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object == self.request.user:
            if request.user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('dashboard')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def getProfileCurrent(self):
        return get_object_or_404(Profile, user=self.request.user)

    def getProfileSlug(self):
        return get_object_or_404(Profile, user=self.object)

    def getDuration(self):
        return getDurationUser(user=self.object)

    def getNumberFollowers(self):
        return getNumberFollowersUser(user=self.object)

    def getHaveCategories(self):
        return getHaveCategoriesUser(user=self.object)

    def getSearchCategories(self):
        return getSearchCategoriesUser(user=self.object)

    def getNoticesHave(self):
        return getNoticesUser(user=self.object, kind=1)

    def getNoticesSearch(self):
        return getNoticesUser(user=self.object, kind=2)

    print('FALTA MOSTRAR ETIQUETAS')
