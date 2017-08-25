from django.db import models
from profiles.models import File
from django.shortcuts import get_object_or_404
# Create your models here.


class Advertising(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to=File.generatePath)

    def searchAdvertising(idAdv):
        return get_object_or_404(Advertising, id=idAdv)
