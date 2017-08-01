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

    def create(tag, profile):
        tagProfile = TagProfile(tag=tag, profile=profile)
        tagProfile.save()
        return tagProfile

    def searchTags(profile):
        return TagProfile.objects.filter(profile=profile).values('tag')

    def searchProfiles(tag):
        return TagProfile.objects.filter(tag=tag).values('profile')

    def foundRepeated(profile, tag):
        return TagProfile.objects.filter(profile=profile, tag=tag).exists()

    def delete(tag, profile):
        return TagProfile.objects.filter(tag=tag, profile=profile).delete()
