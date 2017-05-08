from random import choice
from string import ascii_lowercase, digits
from django.db import models
from django.shortcuts import get_object_or_404
from registration.signals import user_registered
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
# Si hay problemas con null constraint,
# quitar campos del modelo que no han sido anadidos


class Place(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def getCities():
        return Place.objects.exclude(pattern__isnull=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatars/no-avatar.png')
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

    def __str__(self):
        return self.user.username

    def createUser(email, name, last_name, password):
        user, created = User.objects.get_or_create(
            email=email,
            username=Profile.generate_random_username(name),
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

    def searchEmail(email):
        return User.objects.filter(email__iexact=email).exists()

    def searchUser(email):
        return get_object_or_404(User, email=email)

    # Metodo para la generacion del username unico para un nuevo usuario
    def generate_random_username(name, length=16, chars=ascii_lowercase + digits, split=4, delimiter='-'):
        username = ''.join([choice(chars) for i in range(length)])
        if split:
            username = delimiter.join([username[start:start + split] for start in range(0, len(username), split)])
        username = name + '-' + username
        try:
            User.objects.get(username=username)
            return Profile.generate_random_username(name=name, length=length, chars=chars, split=split, delimiter=delimiter)
        except User.DoesNotExist:
            return username

    def user_registered_callback(sender, user, request, **kwargs):
        profile = Profile(user=user)
        # profile.location = get_object_or_404(Place, name=request.POST["location"])
        profile.save(commit=False)

    user_registered.connect(user_registered_callback)
