from django.db import models

# Create your models here.


class Notice(models.Model):
    # Aviso de publicacion de un nuevo producto o servicio
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    # opcion de intercambio
    optionTrade = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Color(models.Model):
    # hexadecimal -> #111111
    name = models.CharField(max_length=7)
    notice = models.ForeignKey(Notice)

    def __str__(self):
        return self.name
