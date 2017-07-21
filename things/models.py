# coding: utf-8

from django.db import models
from profiles.models import Profile, Place
from categories.models import Category
from datetime import datetime
from django.core.validators import validate_comma_separated_integer_list
from django.core.files import File
# Create your models here.


class Notice(models.Model):
    # Aviso de publicacion de un nuevo producto o servicio
    date = models.DateField(default=datetime.now)
    profile = models.ForeignKey(Profile, default="")
    category = models.ForeignKey(Category, default="")
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # KIND: 1 --> propio | 2 --> deseado
    kind = models.IntegerField(default=1)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # la categoria que se envio es la subcategoria, en caso de que no se haya seleccionado se envia la macro

    def create(profile, category, title, description, kind):
        notice = Notice(profile=profile, category=category, title=title, description=description, kind=kind)
        notice.save()
        return notice

    # KIND: 1 --> propio
    def getNoticeType1(profile):
        return Notice.objects.filter(profile=profile, kind=1)

    # KIND: 2 --> deseado
    def getNoticeType2(profile):
        return Notice.objects.filter(profile=profile, kind=2)

    # para unir cosnultas se usa |

    def searchTitle(title, city):
        return CityNotice.searchNotices(city).filter(notice__title__icontains=title).order_by('notice__date')

    def searchCategory(title, category, city):
        return CityNotice.searchNotices(city).filter(notice__title__icontains=title, notice__category=category).order_by('notice__date')


class CityNotice(models.Model):
    # ciudades donde se vera el aviso
    city = models.ForeignKey(Place)
    notice = models.ForeignKey(Notice)

    def create(city, notice):
        cityNotice = CityNotice(city=city, notice=notice)
        cityNotice.save()
        return cityNotice

    def __str__(self):
        return '%s %s' % (self.city, self.notice)

    def searchNotices(city):
        return CityNotice.objects.filter(city=city).order_by('date')

    def searchCities(notice):
        return CityNotice.objects.filter(notice=notice).order_by('date')


class CategoryTrade(models.Model):
    # categorias por las que se quiere intercambiar el bien o servicio
    category = models.ForeignKey(Category)
    notice = models.ForeignKey(Notice)

    def create(category, notice):
        category = CategoryTrade(category=category, notice=notice)
        category.save()
        return category


class Product(models.Model):
    notice = models.OneToOneField(Notice, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    STATE = (
        ('N', 'Nuevo'),
        ('U', 'Usado'),
        ('E', 'Por Encargo'),
        # bring back
        ('B', 'Restaurado'),
        ('R', 'Renovado'),
        ('C', 'Cualquiera'),
    )
    state = models.CharField(max_length=1, choices=STATE, default='N')
    # tamaño - dimensiones
    DELIVERY = (
        ('E', 'Yo mismo lo entrego'),
        ('C', 'Convenio'),
        ('R', 'Redzza service'),
    )
    delivery = models.CharField(max_length=1, choices=DELIVERY, default='C')
    size = models.PositiveIntegerField(blank=True)
    measure = models.CharField(validators=[validate_comma_separated_integer_list], max_length=20, blank=True)
    # a pedido
    order = models.BooleanField(default=False)

    def __str__(self):
        return self.notice

    def create(notice, quantity):
        product = Product(notice=notice, quantity=quantity)
        product.save()
        return product


class Color(models.Model):
    # hexadecimal -> #111111
    hexa = models.CharField(max_length=7)
    product = models.ForeignKey(Product, default="")

    def __str__(self):
        return self.name

    def create(hexa, product):
        color = Color(hexa=hexa, product=product)
        color.save()
        return color


class Service(models.Model):
    notice = models.OneToOneField(Notice, on_delete=models.CASCADE)
    # horas semanales
    time = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.notice

    def create(notice, time):
        service = Service(notice=notice, time=time)
        service.save()
        return service

# https://openwebinars.net/blog/tutorial-django-modelos-bbdd-donde-guardar-informacion/


class Image(models.Model):
    notice = models.ForeignKey(Notice)
    image = models.ImageField(upload_to='productos')
    title = models.CharField(max_length=60, default="")

    def create(notice, title, pathimage):
        image = Image(notice=notice, title=title)
        f = open(pathimage)
        image.image.save(title + '.jpg', File(f))
        image.save()
        return image


class Video(models.Model):
    notice = models.ForeignKey(Notice)
    video = models.FileField(upload_to='videos')

    def create(notice, video):
        video = Video(notice=notice, video=video)
        video.save()
        return video


class Commentary(models.Model):
    commentary = models.CharField(max_length=500)
    notice = models.ForeignKey(Notice)
    profile = models.ForeignKey(Profile)

    def create(commentary, notice, profile):
        commentary = Commentary(commentary=commentary, notice=notice, profile=profile)
        commentary.save()
        return commentary
