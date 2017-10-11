from things.models import Notice, Image, CityNotice, Video, Product, Color
from profiles.models import Profile, Follow, Icon
from string import ascii_lowercase, digits
from random import choice
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework_expiring_authtoken.settings import token_settings
from django.utils import timezone
from django.contrib.auth.models import User
from redzza.site import S3
from redzza.settings import MEDIA_URL
import json
from django.core import serializers
from rest_framework_expiring_authtoken.models import ExpiringToken
from categories.models import WantedCategory
from tags.models import TagProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import itertools


# ---------------------------------METODOS LOGICOS----------------------------------------


# Metodo de verificacion de estructura del email
def validateStructureEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


# Metodo para la generacion del username unico para un nuevo usuario
def generateRandomUsername(name, length=8, chars=ascii_lowercase + digits, split=4, delimiter='-'):
    username = ''.join([choice(chars) for i in range(length)])
    if split:
        username = delimiter.join([username[start:start + split] for start in range(0, len(username), split)])
    username = name + '-' + username
    try:
        User.objects.get(username=username)
        return Profile.generateRandomUsername(name=name, length=length, chars=chars, split=split, delimiter=delimiter)
    except User.DoesNotExist:
        return username


# obtener informacion de message
def getDataMessages(messages):
    context = []
    for message in messages:
        image = str(message.image)
        if image is not '':
            image = S3 + MEDIA_URL + str(message.image)
        context.append({'id': message.id, 'timestamp': message.timestamp, 'text': message.text, 'image': image, 'sender': getProfileSimple([message.sender]), 'conversation': message.conversation.id})
    return context


# obtener data de una lista de categoruas
def getDataCategories(categories):
    context = []
    for category in categories:
        if category.pattern is None:
            context.append({'id': category.id, 'pattern': None, 'name': category.name, 'image': S3 + MEDIA_URL + str(category.image)})
        else:
            context.append({'id': category.id, 'pattern': category.pattern.id, 'name': category.name, 'image': S3 + MEDIA_URL + str(category.image)})
    return context


# obtener data de una lista de cidaddes
def getDataCities(cities):
    context = []
    for city in cities:
        if city.pattern is None:
            context.append({'id': city.id, 'pattern': None, 'name': city.name})
        else:
            context.append({'id': city.id, 'pattern': city.pattern.id, 'name': city.name})
    return context


# obtener data de una lista de cidaddes
def getPlaces(cityNotices):
    context = []
    for cityNotice in cityNotices:
        context.append(cityNotice.city)
    return context


# informacin basica de profile
def getProfileSimple(profiles):
    context = []
    for profile in profiles:
        context.append({'user': profile.user.id, 'profile': profile.id, 'profile_name': profile.user.get_full_name(), 'avatar': S3 + MEDIA_URL + str(profile.avatar)})
    return context


# id - imagen - titulo - kind de listado de notices
def getDataNotice(notices, fullData=True):
    context = []
    data = {}
    for notice in notices:
        images = Image.search(notice)
        if fullData:
            data = noticeComplete(notice)
        if len(images) > 0:
            context.append({'id': notice.id, 'title': notice.title, 'image': S3 + MEDIA_URL + str(images[0].image), 'kind': "%s" % ("i_have" if notice.kind == 1 else "i_search"), 'data': data})
        else:
            context.append({'id': notice.id, 'title': notice.title, 'image': S3 + MEDIA_URL + 'Image/no-image.png', 'kind': "%s" % ("i_have" if notice.kind == 1 else "i_search"), 'data': data})
    return context


# id - imagen - titulo - kind de listado de notices
def noticeComplete(notice):
    context = {}
    context['notice'] = json.loads(serializers.serialize('json', [notice]))
    context['notice'][0]['fields']['location'] = getDataCities([notice.location])
    context['notice'][0]['fields']['profile'] = getProfileSimple([notice.profile])
    context['notice'][0]['fields']['category'] = getDataCategories([notice.category])
    cityNotices = CityNotice.searchCities(notice)
    locations = getPlaces(cityNotices)
    context['notice'][0]['locations'] = getDataCities(locations)
    images = Image.search(notice)
    context['notice'][0]['images'] = []
    if len(images) > 0:
        for i, image in enumerate(images):
            context['notice'][0]['images'].append({'id': str(image.id), 'image': S3 + MEDIA_URL + str(image.image)})
    else:
        context['notice'][0]['images'].append({'image': S3 + MEDIA_URL + 'Image/no-image.png'})
    videos = Video.search(notice)
    context['notice'][0]['videos'] = []
    for i, video in enumerate(videos):
        context['notice'][0]['videos'].append({'id': str(video.id), 'video': S3 + MEDIA_URL + str(video.video)})
    thing = Notice.sortoutNotices([notice], False)[0]
    context['notice'][0]['thing'] = json.loads(serializers.serialize('json', [thing]))
    if thing.__class__ == Product:
        colors = Color.searchProduct(thing)
        context['notice'][0]['thing'][0]['fields']['colors'] = []
        for i, color in enumerate(colors):
            context['notice'][0]['thing'][0]['fields']['colors'].append({'color': str(color.hexa)})
    return context


# obtencion de notices de una lista tipo query
def noticesQuery(queries):
    notices = []
    for query in queries:
        if query is not None:
            for element in query:
                if element.__class__ is Notice:
                    notices.append(element)
                else:
                    notices.append(element.notice)
    notices = removeDuplicates(notices)
    i_have = [notice for notice in notices if notice.kind == 1]
    i_search = [notice for notice in notices if notice.kind == 2]
    return [x for x in itertools.chain.from_iterable(itertools.zip_longest(i_have, i_search)) if x]


def removeDuplicates(notices):
    seen = set()
    seen_add = seen.add
    return [x for x in notices if not (x in seen or seen_add(x))]


def getPagination(context, request, size):
    page = request.GET.get('page', 1)
    paginator = Paginator(context, size)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = "Page not an integer"
    except EmptyPage:
        data = "Empty Page"
    return data

# ---------------------------------METODOS OBTENCION DE DATOS---------------------------------


# Metodo de obtencion de perfil de usuario
def getProfile(user):
    return get_object_or_404(Profile, user=user)


# Metodo de obtencion de token de usuario
def getToken(user):
    token, _ = ExpiringToken.objects.get_or_create(user=user)
    if token.expired():
        token.delete()
        token = ExpiringToken.objects.create(user=user)
    return token


# Metodo de obtencion de usuario
def getUser(id):
    return Profile.getUser(id)


# Metodo de obtencion de usuario
def getUserEmail(email):
    return Profile.getUserEmail(email)


# Metodo que retorna el tiempo inscrito en redzza del usuario ingresado por parametro
def getDurationUser(user):
    return (timezone.now() - user.date_joined)


# Metodo que retorna el numero de seguidores del usuario ingresado por parametro
def getNumberFollowersUser(user):
    return len(Follow.searchFollowers(getProfile(user)))


# Metodo que retorna las categorias que ofrece el usuario ingresado por parametro
# i_have(Ofrezco) --> 1
def getHaveCategoriesUser(user):
    return WantedCategory.searchHave(getProfile(user))


# Metodo que retorna las categorias que busca el usuario ingresado por parametro
# i_search(Busco) --> 2
def getSearchCategoriesUser(user):
    return WantedCategory.searchOffer(getProfile(user))


# Metodo que retorna todas las notices de un usuarios
def getNoticesUser(user):
    return Notice.getNoticeProfile(getProfile(user))


# Metodo que retorna las publicaciones del usuario tiene
def getNoticesHaveUser(user):
    return Notice.getNoticeHave(getProfile(user))


# Metodo que retorna las publicaciones del usuario busca
def getNoticesSearchUser(user):
    return Notice.getNoticeSearch(getProfile(user))


# Metodo que retorna los tags del usuario
def getTagsUser(user):
    return TagProfile.searchTags(getProfile(user))


# Metodo que retorna el icono del usuario
def getIconUser(user):
    return Icon.searchIcono(getProfile(user).icono)


# Metodo que imagen de una notice
def getImageNotice(notice):
    return Image.search(notice)


# Metodo de obtencion de tiempo restante del token de usuario
def getTimeToken(token):
    return token_settings.EXPIRING_TOKEN_LIFESPAN - (timezone.now() - token.created)
