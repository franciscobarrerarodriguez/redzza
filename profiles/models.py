from django.db import models
from registration.signals import user_registered
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatars/no-avatar.png')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.user

    def user_registered_callback(sender, user, request, **kwargs):
        profile = Profile(user=user)
        profile.save()

    user_registered.connect(user_registered_callback)
