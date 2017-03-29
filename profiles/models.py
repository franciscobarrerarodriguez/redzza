from django.db import models
from registration.signals import user_registered
from django.contrib.auth.models import User
from datetime import datetime   
# Create your models here.

class Place(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatars/no-avatar.png')
    birth_date = models.DateField(null=True, blank=True)
    #No son opcionales
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Place, default="")
    biography = models.TextField(blank=True) #opcional

    def __unicode__(self):
        return self.user

    def user_registered_callback(sender, user, request, **kwargs):
        profile = Profile(user = user)
        profile.location = get_object_or_404(Place, name=request.POST["location"])  
        profile.save()

    user_registered.connect(user_registered_callback)
