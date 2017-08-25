# coding: utf-8

from django.db import models
from profiles.models import File, Profile, Place
from categories.models import Category
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.


class Notice(models.Model):
    # Aviso de publicacion de un nuevo producto o servicio
    date = models.DateField(default=datetime.now)
    profile = models.ForeignKey(Profile, default="")
    category = models.ForeignKey(Category, default="")
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # si recibe u ofrece dinero a cambio
    money = models.BooleanField(default=True)
    # oferta preferente para el intercambio
    offer = models.ForeignKey("self", blank=True, null=True)
    # KIND: 1 --> propio | 2 --> deseado
    kind = models.IntegerField(default=1)
    visibility = models.BooleanField(default=True)
    # urgente un tiempo 24 horas
    urgency = models.BooleanField(default=False)
    # lugar donde se encuentra el producto o se presta el servicio
    location = models.ForeignKey(Place, default="")

    def __str__(self):
        return self.title

    def create(profile, idCategory, title, description, kind, urgency, place):
        category = get_object_or_404(Category, id=idCategory)
        location = get_object_or_404(Place, id=place)
        notice = Notice(profile=profile, category=category, title=title, description=description, kind=kind, urgency=urgency, location=location)
        notice.save()
        return notice

    def getNotice(id):
        return Notice.objects.get(id=id)

    def getNoticeProfile(profile):
        return Notice.objects.filter(profile=profile)

    def getNoticeHave(profile):
        return Notice.objects.filter(profile=profile, kind=1)

    def getNoticeSearch(profile):
        return Notice.objects.filter(profile=profile, kind=2)

    def updateLocation(notice, place):
        location = get_object_or_404(Place, id=place)
        notice.location = location
        return notice.save()

    def updateOffer(notice, offer):
        noticeOffer = get_object_or_404(Notice, id=offer)
        notice.offer = noticeOffer
        return notice.save()

    def updateCategory(notice, idCategory):
        category = get_object_or_404(Category, id=idCategory)
        notice.category = category
        return notice.save()

    def updatePlace(notice, place):
        location = get_object_or_404(Place, id=place)
        notice.location = location
        return notice.save()

    def updateTitle(notice, title):
        notice.title = title
        return notice.save()

    def updateUrgency(notice, urgency):
        notice.urgency = urgency
        return notice.save()

    def updateVisibility(notice, visibility):
        notice.visibility = visibility
        return notice.save()

    def updateDescription(notice, description):
        notice.description = description
        return notice.save()
    # para unir consultas se usa |

    # buscar avisos por personas a las que sigue
    def searchFollowing(following):
        notices = Notice.objects.filter(profile=following[0])
        for f in range(1, len(following)):
            notices = notices | Notice.objects.filter(profile=following[f])
        print(len(notices))
        result = notices.order_by('date')
        return result

    def searchTitle(title, kind):
        return Notice.objects.filter(title__icontains=title, kind=kind).order_by('date')

    def searchCity(city, kind):
        return CityNotice.searchNotices(city).filter(notice__kind=kind).order_by('notice__date')

    def searchCategory(category, kind):
        result = None
        if category.pattern is not None:
            result = Notice.objects.filter(category=category, kind=kind)
        else:
            result = Notice.objects.filter(category__pattern=category, kind=kind) | Notice.objects.filter(category=category, kind=kind)
        return result.order_by('date')

    # buscar avisos por título y por ciudad
    def searchTitleCity(title, city, kind):
        return CityNotice.searchNotices(city).filter(notice__title__icontains=title, notice__kind=kind).order_by('notice__date')

    def searchTitleCategory(title, category, kind):
        result = None
        if category.pattern is not None:
            result = Notice.objects.filter(title__icontains=title, category=category, kind=kind)
        else:
            result = Notice.objects.filter(title__icontains=title, category__pattern=category, kind=kind) | Notice.objects.filter(title__icontains=title, category=category, kind=kind)
        return result.order_by('notice__date')

    def searchCategoryCity(category, city, kind):
        result = None
        if category.pattern is not None:
            result = CityNotice.searchNotices(city).filter(notice__category=category, notice__kind=kind)
        else:
            result = CityNotice.searchNotices(city).filter(notice__category__pattern=category, notice__kind=kind) | CityNotice.searchNotices(city).filter(notice__category=category, notice__kind=kind)
        return result.order_by('notice__date')

    # faltan queries con array
    # hacer una lista combinada de productos y servicios
    # buscar avisos por categoría y por ciudad
    def searchTitleCategoryCity(title, category, city, kind):
        result = None
        if category.pattern is not None:
            result = CityNotice.searchNotices(city).filter(notice__title__icontains=title, notice__category=category, notice__kind=kind)
        else:
            result = CityNotice.searchNotices(city).filter(notice__title__icontains=title, notice__category__pattern=category, notice__kind=kind) | CityNotice.searchNotices(city).filter(notice__title__icontains=title, notice__category=category, notice__kind=kind)
        return result.order_by('notice__date')

    def sortoutNotices(notices, city):
        result = []
        for n in notices:
            if city is True:
                notice = n.notice
            else:
                notice = n
            if Product.searchProduct(notice) is None:
                if Service.searchService(notice) is None:
                    # si no tiene relación con ninguno es un servicio sin tiempo de horas semanales
                    result.append(notice)
                else:
                    result.append(Service.searchService(notice))
            else:
                result.append(Product.searchProduct(notice))
        return result


class CityNotice(models.Model):
    # ciudades donde se vera el aviso
    city = models.ForeignKey(Place)
    notice = models.ForeignKey(Notice)

    def __str__(self):
        return '%s %s' % (self.city, self.notice)

    def create(location, notice):
        city = get_object_or_404(Place, id=location)
        cityNotice = CityNotice(city=city, notice=notice)
        cityNotice.save()
        return cityNotice

    def deleteAll(notice):
        CityNotice.objects.filter(notice=notice).delete()

    # falta resolver los departamentos
    def searchNotices(city):
        return CityNotice.objects.filter(city=city)

    def searchCities(notice):
        return CityNotice.objects.filter(notice=notice)


class Product(models.Model):
    notice = models.OneToOneField(Notice, on_delete=models.CASCADE)
    STATE = (
        ('N', 'Nuevo'),
        ('U', 'Usado'),
        ('E', 'Por Encargo'),
        ('B', 'Restaurado'),
        ('R', 'Reparado'),
        ('M', 'Mejorado'),
        ('C', 'Cualquiera'),
    )
    state = models.CharField(max_length=1, choices=STATE, default='N')
    DELIVERY = (
        ('E', 'Yo mismo lo entrego'),
        ('C', 'Convenio'),
        ('R', 'Redzza service'),
    )
    delivery = models.CharField(max_length=1, choices=DELIVERY, default='C')

    def __str__(self):
        return self.notice.title

    def create(notice, state):
        product = Product(notice=notice, state=state)
        product.save()
        return product

    def updateState(product, state):
        product.state = state
        return product.save()

    def searchProduct(notice):
        try:
            return Product.objects.get(notice=notice)
        except Exception as e:
            return None


class Color(models.Model):
    # hexadecimal -> #111111
    hexa = models.CharField(max_length=7)
    product = models.ForeignKey(Product, default="")

    def __str__(self):
        return self.hexa

    def create(hexa, product):
        color = Color(hexa=hexa, product=product)
        color.save()
        return color

    def deleteAll(product):
        Color.objects.filter(product=product).delete()

    def searchProduct(product):
        return Color.objects.filter(notice=product)


class Service(models.Model):
    notice = models.OneToOneField(Notice, on_delete=models.CASCADE)
    # horas semanales
    time = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.notice.title

    def create(notice, time):
        service = Service(notice=notice, time=time)
        service.save()
        return service

    def updateTime(service, time):
        service.time = time
        return service.save()

    def searchService(notice):
        try:
            return Service.objects.get(notice=notice)
        except Exception as e:
            return None


class Image(models.Model):
    notice = models.ForeignKey(Notice)
    image = models.ImageField(upload_to=File.generatePath)

    def create(notice, pathfile):
        image = Image(notice=notice, image=pathfile)
        image.save()
        return image

    def search(notice):
        return Image.objects.filter(notice=notice)

# metodo para borrar archivos cuando se borre el registro


@receiver(post_delete, sender=Image)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.image.delete(False)


class Video(models.Model):
    # archivo o url
    notice = models.ForeignKey(Notice)
    video = models.FileField(upload_to=File.generatePath)

    def create(notice, pathfile):
        video = Video(notice=notice, video=pathfile)
        video.save()
        return video

    def search(notice):
        return Video.objects.filter(notice=notice)


# metodo para borrar archivos cuando se borre el registro
@receiver(post_delete, sender=Video)
def video_delete(sender, instance, **kwargs):
    """ Borra los ficheros de los videos que se eliminan. """
    instance.video.delete(False)


class Commentary(models.Model):
    commentary = models.CharField(max_length=500)
    notice = models.ForeignKey(Notice)
    profile = models.ForeignKey(Profile)

    def create(commentary, notice, profile):
        commentary = Commentary(commentary=commentary, notice=notice, profile=profile)
        commentary.save()
        return commentary

    def search(notice):
        return Commentary.objects.filter(notice=notice)

    def searchHistory(profile):
        return Commentary.objects.filter(profile=profile)
