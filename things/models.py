# coding: utf-8

from django.db import models
from profiles.models import Profile, Place
from categories.models import Category
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.


class Notice(models.Model):
    # Aviso de publicacion de un nuevo producto o servicio
    date = models.DateField(default=datetime.now)
    profile = models.ForeignKey(Profile, default="")
    category = models.ForeignKey(Category, default="")
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # si recibe u ofrece dinero a cambio
    money = models.BooleanField(default=True)
    # oferta preferente para el intercambio
    offer = models.ForeignKey("self", blank=True, null=True)
    # KIND: 1 --> propio | 2 --> deseado
    kind = models.IntegerField(default=1)
    visibility = models.BooleanField(default=True)
    # urgente un tiempo 24 horas
    urgency = models.BooleanField(default=False)


class CityNotice(models.Model):
    # ciudades donde se vera el aviso
    city = models.ForeignKey(Place)
    notice = models.ForeignKey(Notice)

    def __str__(self):
        return '%s %s' % (self.city, self.notice)


class Product(models.Model):
    notice = models.OneToOneField(Notice, on_delete=models.CASCADE)
    STATE = (
        ('N', 'Nuevo'),
        ('U', 'Usado'),
        ('E', 'Por Encargo'),
        ('B', 'Restaurado'),
        ('R', 'Reparado'),
        ('M', 'Mejorado'),
        ('C', 'Cualquiera'),
    )
    state = models.CharField(max_length=1, choices=STATE, default='N')
    DELIVERY = (
        ('E', 'Yo mismo lo entrego'),
        ('C', 'Convenio'),
        ('R', 'Redzza service'),
    )
    delivery = models.CharField(max_length=1, choices=DELIVERY, default='C')

    def __str__(self):
        return self.notice


class Color(models.Model):
    # hexadecimal -> #111111
    hexa = models.CharField(max_length=7)
    product = models.ForeignKey(Product, default="")

    def __str__(self):
        return self.name


class Service(models.Model):
    notice = models.OneToOneField(Notice, on_delete=models.CASCADE)
    # horas semanales
    time = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.notice


class Image(models.Model):
    notice = models.ForeignKey(Notice)
    image = models.ImageField(upload_to='productos')


# metodo para borrar archivos cuando se borre el registro
@receiver(post_delete, sender=Image)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.image.delete(False)


class Video(models.Model):
    # archivo o url
    notice = models.ForeignKey(Notice)
    video = models.FileField(upload_to='videos')


# metodo para borrar archivos cuando se borre el registro
@receiver(post_delete, sender=Video)
def video_delete(sender, instance, **kwargs):
    """ Borra los ficheros de los videos que se eliminan. """
    instance.video.delete(False)


class Commentary(models.Model):
    commentary = models.CharField(max_length=500)
    notice = models.ForeignKey(Notice)
    profile = models.ForeignKey(Profile)
