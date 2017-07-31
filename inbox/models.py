from django.db import models
from profiles.models import Profile
from things.models import Notice
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)


class TagProfile(models.Model):
    profile = models.ForeignKey(Profile, default="")
    tag = models.ForeignKey(Tag, default="")


class TagNotice(models.Model):
    tag = models.ForeignKey(Tag, default="")
    notice = models.ForeignKey(Notice, default="")
