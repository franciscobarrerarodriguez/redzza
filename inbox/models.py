from django.db import models
from profiles.models import Profile


class Conversation(models.Model):
    modified = models.DateTimeField(auto_now=True)
    user = models.ManytoManyField(Profile)


class Message(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField()
    image = models.ImageField()
    review = models.BooleanField()
    user = models.ForeignKey(Profile)
    conversation = models.ForeignKey(Conversation)
