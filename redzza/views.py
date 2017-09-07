# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
# Create your views here.
from categories.models import WantedCategory, Category
from profiles.models import Profile, Place, Follow
from things.models import Notice, Image, Video
from inbox.models import Conversation, Message
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import requests
import json


def fillPlaces():
    prueba = []
    places = requests.get("https://raw.githubusercontent.com/marcovega/colombia-json/master/colombia.json")
    for dpto in places.json():
        pattern = Place(name=dpto.get('departamento'))
        pattern.save()
        for city in dpto.get('ciudades'):
            town = Place(name=city, pattern=pattern)
            town.save()
    return prueba


def queries(request):
    # profile = get_object_or_404(Profile, gender='F')
    # oldcategory = get_object_or_404(Category, name="Vehiculos - Motos")
    # Vehiculos - Motos
    # category = get_object_or_404(Category, name="Seguridad")
    # query = Profile.updateBirthdate(get_object_or_404(Profile, gender='F'), "2015-11-06")
    # query = Profile.updateGender(get_object_or_404(Profile, gender='F'), 'M')
    # tunja -> 3
    # if LabelProfile.foundRepeated(get_object_or_404(Profile, gender='F'), get_object_or_404(Label, id=1)) is False:
    #    query = LabelProfile.create(get_object_or_404(Label, id=1), get_object_or_404(Profile, gender='F'))
    # else:
    #    query = LabelProfile.delete(get_object_or_404(Label, id=1), get_object_or_404(Profile, gender='F'))
    # query = Notice.create(get_object_or_404(Profile, gender='F'), Category.objects.get(id=60), "carro renault 4", "mi carrito de siempre", 1)
    # query = Notice.searchTitle("arro", Place.searchCity(3))
    # query = Notice.sortoutNotices(Notice.objects.all())
    # notice = get_object_or_404(Notice, title="carro renault 4")
    # query = Image.create(notice, "/home/diego/2.jpg")
    # query = Video.create(notice, "/home/diego/Documents/redzza/redzza/media/videos/Gorillaz.mp4")
    # para acceder a la url de la imagen se accede a Image.image.name
    # query = WantedCategory.updateHave(profile, oldcategory, category)
    # query = Notice.searchTitleCategoryCity("o", oldcategory.id, Place.searchCity(3).id, 1)
    # query = Conversation.countNotifications(get_object_or_404(Profile, user__username="d"))
    # query = Message.create("hola", None, get_object_or_404(Profile, user__username="d"), prueba)
    # query = Conversation.search(get_object_or_404(Profile, user__username="d"))
    # query = Message.search(get_object_or_404(Conversation, id=16))
    # query = Conversation.checkExistence(Profile.objects.all())
    # 16
    # query = Place.getDepartments()
    return HttpResponse()
    # type -> tipo de campo
    # dir atributos de la clase
