from django.db import models
from profiles.models import Profile, File
from things.models import Notice
from django.db.models.signals import post_save
from django.dispatch import receiver


class Conversation(models.Model):
    # hora del ultimo mensaje enviado
    modified = models.DateTimeField(auto_now_add=True)
    contestant = models.ManyToManyField(Profile)
    notice = models.ManyToManyField(Notice)

    def __str__(self):
        return str(self.modified)

    def create(profiles, notice):
        if Conversation.checkExistence(profiles) is False:
            conversation = Conversation()
            conversation.save()
            for p in profiles:
                conversation.contestant.add(p)
            conversation.notice.add(notice)
            return conversation
        else:
            conversation = Conversation.objects.filter(contestant__in=profiles).distinct()
            conversation[0].notice.add(notice)
            return conversation, "update"

    def search(profile):
        return Conversation.objects.filter(contestant=profile).order_by('modified')

    def checkExistence(profiles):
        return Conversation.objects.filter(contestant__in=profiles).exists()


class Message(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=File.generatePath, blank=True, null=True)
    review = models.BooleanField(default=False)
    sender = models.ForeignKey(Profile)
    conversation = models.ForeignKey(Conversation)

    def __str__(self):
        return self.text

    def create(text, image, profile, conversation):
        message = Message(text=text, image=image, sender=profile, conversation=conversation)
        message.save()
        return message

    def search(conversation):
        return Message.objects.filter(conversation=conversation).order_by('timestamp')


@receiver(post_save, sender=Message)
def update_modified(sender, instance, **kwargs):
    """ Actualiza el tiempo del modified en una conversación """
    instance.conversation.modified = instance.timestamp
    instance.conversation.save()
