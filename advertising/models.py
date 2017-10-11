from django.db import models
from profiles.models import File
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.db.models.signals import post_init
# Create your models here.


class Advertising(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to=File.generatePath)
    counter = models.IntegerField(default=0)

    def searchAdvertising(idAdv):
        return get_object_or_404(Advertising, id=idAdv)

    def increaseCounter(idAdv):
        adv = Advertising.searchAdvertising(idAdv)
        adv.counter += 1
        return adv.counter
