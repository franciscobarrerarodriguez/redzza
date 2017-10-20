from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date
# usada para acceder a los archivos
import os
# usado para generar el nombre de una imagen
from uuid import uuid4


class File():
    def generatePath(instance, filename):
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo, se usa el nombre de la clase y la fecha actual.
        directorio_clase = instance.__class__.__name__
        ruta = os.path.join(directorio_clase)

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(
            date.today().strftime("%Y-%m-%d") + "-" + uuid4().hex, extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)


class Place(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def getDepartments():
        return Place.objects.filter(pattern=None)

    def searchTowns(department):
        return Place.objects.filter(pattern=department).order_by('name')

    def searchPlace(idLocation):
        return get_object_or_404(Place, id=idLocation)

    def searchName(name):
        return Place.objects.get(name=name)


class Icon(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='iconos', default='Icon/icono.png')

    def searchIcono(idIcono):
        return get_object_or_404(Icon, id=idIcono)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=File.generatePath, default='Profile/no-avatar.png')
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

    def getUser(id):
        return get_object_or_404(User, id=id)

    def getUserEmail(email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def searchEmail(email):
        return User.objects.filter(email__iexact=email).exists()

    def searchUsername(username):
        return User.objects.filter(username__iexact=username).exists()

    def updateAvatar(profile, avatar):
        # profile.avatar.avatar_delete
        profile.avatar = avatar
        return profile.save()

    def updateIcono(profile, idIcono):
        icono = Icon.searchIcono(idIcono)
        profile.icono = icono
        return profile.save()

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
        place = Place.searchPlace(location)
        profile.location = place
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

# metodo para borrar archivos de los avatar cuando se borre el registro


@receiver(pre_save, sender=Profile)
def avatar_delete(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding 'Profile' object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Profile.objects.get(pk=instance.pk).avatar
    except Profile.DoesNotExist:
        return False
    if not old_file == "Profile/no-avatar.png":
        new_file = instance.avatar
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


class Follow(models.Model):
    following = models.ForeignKey(Profile, related_name="following")
    follower = models.ForeignKey(Profile, related_name="follower")

    def __str__(self):
        return '%s %s' % (self.following, self.follower)

    def searchFollowers(profile):
        return Follow.objects.filter(following=profile).values('follower')

    def searchFollowings(profile):
        return Follow.objects.filter(follower=profile).values('following')

    def checkFollowing(follower, following):
        return Follow.objects.filter(follower=follower, following=following).exists()

    def getFollowing(follower, following):
        return Follow.objects.filter(follower=follower, following=following)
