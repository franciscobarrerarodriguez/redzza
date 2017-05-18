# coding: utf-8

from django.db import models
from profiles.models import Profile, Place
from categories.models import Category

# Create your models here.


class Notice(models.Model):
    profile = models.ForeignKey(Profile, default="")
    category = models.ForeignKey(Category, default="")
    # Aviso de publicacion de un nuevo producto o servicio
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    # opcion de intercambio
    optionTrade = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def create(profile, category, title, description, optionTrade):
        notice = Notice(profile=profile, category=category, title=title)
        notice.save()
        return notice

    def getNotice(profile):
        return Notice.objects.filter(profile=profile)


class CityNotice(models.Model):
    # ciudades donde se vera el aviso
    city = models.ForeignKey(Place)
    notice = models.ForeignKey(Notice)

    def create(city, notice):
        cityNotice = CityNotice(city=city, notice=notice)
        cityNotice.save()
        return cityNotice


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
        ('N', 'Renovado'),
    )
    state = models.CharField(max_length=1, choices=STATE, default='Nuevo')
    # tamaño - dimensiones
    DELIVERY = (
        ('E', 'Yo mismo lo entrego'),
        ('C', 'Convenio'),
        ('R', 'Redzza service'),
    )
    delivery = models.CharField(max_length=1, choices=DELIVERY, default='Convenio')
    size = models.PositiveIntegerField(blank=True)
    measure = models.CommaSeparatedIntegerField(max_length=20, blank=True)
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


class Image(models.Model):
    notice = models.ForeignKey(Notice)
    image = models.ImageField()

    def create(notice, image):
        image = Image(notice=notice, image=image)
        image.save()
        return image


class Video(models.Model):
    notice = models.ForeignKey(Notice)
    video = models.FileField(upload_to='uploads')

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
