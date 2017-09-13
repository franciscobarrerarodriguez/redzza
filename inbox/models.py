from django.db import models
from profiles.models import Profile, File
from things.models import Notice
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from django.dispatch import receiver


class Conversation(models.Model):
    # hora del ultimo mensaje enviado
    modified = models.DateTimeField(auto_now_add=True)
    contestant = models.ManyToManyField(Profile, related_name='contestant')
    notice = models.ManyToManyField(Notice)
    review = models.ManyToManyField(Profile, related_name='review', blank=True)

    def __str__(self):
        return str(self.modified)

    def getConversation(idConversation):
        return Conversation.objects.get(id=idConversation)

    def create(profiles, notice):
        existence = Conversation.checkExistence(profiles, notice)
        if existence.exists() is False:
            conversation = Conversation()
            conversation.save()
            for p in profiles:
                conversation.contestant.add(p)
            conversation.notice.add(notice)
            return [conversation], ""
        else:
            return existence, "update"

    def search(profile):
        return Conversation.objects.filter(contestant=profile).order_by('-modified')

    # notificaciones
    def countNotifications(profile):
        return Conversation.objects.filter(contestant=profile).exclude(review=profile).count()

    def addReview(idProfile, idConversation):
        profile = get_object_or_404(Profile, id=idProfile)
        return Conversation.getConversation(idConversation).review.add(profile)

    def checkExistence(profiles, notice):
        result = Conversation.objects.filter(contestant=profiles[0], notice=notice)
        for p in range(1, len(profiles)):
            result = result.filter(contestant=profiles[p])
        return result


class Message(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=File.generatePath, blank=True, null=True)
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

    def searchConversationsSend(profile):
        return Message.objects.filter(sender=profile).order_by('timestamp')


@receiver(post_save, sender=Message)
def update_conversation(sender, instance, **kwargs):
    """ Actualiza el tiempo del modified y el review(sender) en una conversación """
    try:
        instance.conversation.modified = instance.timestamp
        instance.conversation.review.clear()
        instance.conversation.review.add(instance.sender)
        instance.conversation.save()
    except Exception as e:
        pass
