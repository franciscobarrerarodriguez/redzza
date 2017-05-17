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


class CityNotice(models.Model):
    # ciudades donde se vera el aviso
    city = models.ForeignKey(Place)
    notice = models.ForeignKey(Notice)


class CategoryTrade(models.Model):
    # categorias por las que se quiere intercambiar el bien o servicio
    category = models.ForeignKey(Category)
    notice = models.ForeignKey(Notice)


class Product(models.Model):
    notice = models.OneToOneField(Notice, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    STATE = (
        ('N', 'Nuevo'),
        ('U', 'Usado'),
        ('R', 'Reparado'),
    )
    state = models.CharField(max_length=8, choices=STATE, default='Nuevo')
    # tamaño - dimensiones
    size = models.PositiveIntegerField(blank=True)
    measure = models.CommaSeparatedIntegerField(max_length=20, blank=True)
    # a pedido
    order = models.BooleanField(default=False)

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
