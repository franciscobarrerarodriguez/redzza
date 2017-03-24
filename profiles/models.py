from __future__ import unicode_literals

from django.db import models

from registration.signals import user_registered
 # Create your models here.
class User(models.Model):
    mail = models.EmailField(unique=True)    
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)    
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class Profile(models.Model):
    user = models.ForeignKey(User)
    is_human = models.BooleanField()
 
    def __unicode__(self):
        return self.user

    def user_registered_callback(sender, user, request, **kwargs):
        profile = Profile(user = user)
        profile.is_human = bool(request.POST["is_human"])
        profile.save()
     
    user_registered.connect(user_registered_callback)