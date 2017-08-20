from django.db import models
from profiles.models import Profile
from django.shortcuts import get_object_or_404
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TagProfile(models.Model):
    # etiquetas asignadas a las personas
    profile = models.ForeignKey(Profile, default="", related_name='profile')
    tag = models.ForeignKey(Tag, default="", related_name='tag')

    # faltan mostrar todas las etiquetas
    
    def __str__(self):
        return '%s %s' % (self.tag, self.profile)

    def create(element, profile):
        tag = get_object_or_404(Tag, id=element)
        tagProfile = TagProfile(profile=profile, tag=tag)
        return tagProfile.save()

    def deleteAll(profile):
        TagProfile.objects.filter(profile=profile).delete()

    def searchTags(profile):
        return TagProfile.objects.filter(profile=profile).values('tag')
