from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import get_object_or_404


class Place(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatars/no-avatar.png')
    icono = models.ImageField(upload_to='iconos', default='iconos/icono.png')
    birth_date = models.DateField(default=datetime.now)
    GENDER = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER, default='M')
    phone = models.IntegerField(null=True, blank=True)
    biography = models.TextField(blank=True)  # opcional
    location = models.ForeignKey(Place, default="")
    company = models.CharField(max_length=40, blank=True)
    profession = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=40, blank=True)
    avialability = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username

    def searchEmail(email):
        return User.objects.filter(email__iexact=email).exists()

    def createUser(email, username, name, last_name, password):
        user, created = User.objects.get_or_create(
            email=email,
            username=username,
            first_name=name,
            last_name=last_name
        )
        if created:
            user.set_password(password)
            user.save()
        return user, created

    def create(place, user):
        location = get_object_or_404(Place, id=place)
        profile = Profile(user=user, location=location)
        profile.save()
        return profile


class Follow(models.Model):
    following = models.ForeignKey(Profile, related_name="following")
    follower = models.ForeignKey(Profile, related_name="follower")

    def __str__(self):
        return '%s %s' % (self.following, self.follower)
