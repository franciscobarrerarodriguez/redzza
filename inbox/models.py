from django.db import models
from profiles.models import Profile


class Conversation(models.Model):
    modified = models.DateTimeField(auto_now_add=True)
    contestant = models.ManyToManyField(Profile)

    def create(profiles):
        conversation = Conversation()
        conversation.save()
        for p in profiles:
            conversation.contestant.add(p)
        return conversation


class Message(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField()
    review = models.BooleanField()
    contestant = models.ForeignKey(Profile)
    conversation = models.ForeignKey(Conversation)
