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

    def searchCity(location):
        return get_object_or_404(Place, id=location)


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
    # horario de atencion
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

    def search(user):
        return Profile.objects.filter(user=user)

    def updatePhone(profile, phone):
        profile.phone = phone
        return profile.save()

    def updateAvialability(profile, avialability):
        profile.avialability = avialability
        return profile.save()

    def updateAdress(profile, address):
        profile.address = address
        return profile.save()

    def updateProfession(profile, profession):
        profile.profession = profession
        return profile.save()

    def updateCompany(profile, company):
        profile.company = company
        return profile.save()

    def updateBiography(profile, biography):
        profile.biography = biography
        return profile.save()

    def updateGender(profile, gender):
        profile.gender = gender
        return profile.save()

    def updateBirthdate(profile, date):
        profile.birth_date = date
        return profile.save()

    def updateLocation(profile, location):
        profile.location = location
        return profile.save()

    def searchEmail(email):
        return User.objects.filter(email__iexact=email).exists()

    def searchUsername(username):
        return User.objects.filter(username__iexact=username).exists()

    def searchUser(email):
        return get_object_or_404(User, email=email)


class Label(models.Model):
    label = models.CharField(max_length=50)


class LabelProfile(models.Model):
    label = models.ForeignKey(Label)
    profile = models.ForeignKey(Profile)

    def create(label, profile):
        labelProfile = LabelProfile(label=label, profile=profile)
        labelProfile.save()
        return labelProfile

    def searchLabels(profile):
        return LabelProfile.objects.filter(profile__iexact=profile)

    def searchProfiles(label):
        return LabelProfile.objects.filter(label__iexact=label)

    def delete(profile, label):
        labelProfile = get_object_or_404(LabelProfile, profile=profile, label=label)
        return labelProfile.delete()


class Follow(models.Model):
    following = models.ForeignKey(Profile, related_name="following")
    follower = models.ForeignKey(Profile, related_name="follower")

    def create(profile1, profile2):
        follow = Follow(following=profile1, follower=profile2)
        follow.save()
        return follow
