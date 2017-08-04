from django.db import models
from profiles.models import Profile
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TagProfile(models.Model):
    # etiquetas asignadas a las personas
    profile = models.ForeignKey(Profile, default="", related_name='profile')
    tag = models.ForeignKey(Tag, default="", related_name='tag')

    def __str__(self):
        return '%s %s' % (self.tag, self.profile)
