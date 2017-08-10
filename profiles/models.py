from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import get_object_or_404


class Place(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def searchCity(location):
        return get_object_or_404(Place, id=location)


class Icon(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='iconos', default='iconos/icono.png')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatars/no-avatar.png')
    icono = models.ForeignKey(Icon, blank=True, null=True)
    birth_date = models.DateField(default=datetime.now)
    GENDER = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER, default='M')
    phone = models.CharField(max_length=20, blank=True)
    # phone = models.BigIntegerField(default=0, blank=True)
    biography = models.TextField(blank=True)  # opcional
    location = models.ForeignKey(Place, default="")
    company = models.CharField(max_length=40, blank=True)
    profession = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=40, blank=True)
    avialability = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username

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

    def searchEmail(email):
        return User.objects.filter(email__iexact=email).exists()

    def searchUsername(username):
        return User.objects.filter(username__iexact=username).exists()

    def updateAvatar(profile, avatar):
        print('falta update avatar')

    def updateIcono(profile, icono):
        print('falta update icono')

    def updateBirthdate(profile, date):
        profile.birth_date = date
        return profile.save()

    def updateGender(profile, gender):
        profile.gender = gender
        return profile.save()

    def updatePhone(profile, phone):
        profile.phone = phone
        return profile.save()

    def updateBiography(profile, biography):
        profile.biography = biography
        return profile.save()

    def updateLocation(profile, location):
        profile.location = location
        return profile.save()

    def updateCompany(profile, company):
        profile.company = company
        return profile.save()

    def updateProfession(profile, profession):
        profile.profession = profession
        return profile.save()

    def updateAddress(profile, address):
        profile.address = address
        return profile.save()

    def updateAvialability(profile, avialability):
        profile.avialability = avialability
        return profile.save()


class Follow(models.Model):
    following = models.ForeignKey(Profile, related_name="following")
    follower = models.ForeignKey(Profile, related_name="follower")

    def __str__(self):
        return '%s %s' % (self.following, self.follower)
