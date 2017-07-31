from django.db import models
from profiles.models import Profile
from django.shortcuts import get_object_or_404
# Create your models here.


class Category(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=28)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def getCategories():
        return Category.objects.filter(pattern__isnull=True).order_by('name')

    def getSubCategories():
        return Category.objects.exclude(pattern__isnull=True).order_by('name')

    def getSeconds(category):
        return Category.objects.filter(pattern=category).order_by('name')


class WantedCategory(models.Model):
    category = models.ForeignKey(Category)
    profile = models.ForeignKey(Profile)
    # Offer(Ofrezco) --> 1 ; Search(Busco) --> 2
    type_category = models.IntegerField()

    def __str__(self):
        return str(self.category)

    def create(element, profile, kind):
        category = get_object_or_404(Category, id=element)
        wanted = WantedCategory(profile=profile, category=category, type_category=kind)
        return wanted.save()

    @staticmethod
    def searchHave(profile):
        return WantedCategory.objects.filter(profile=profile, type_category=1)

    @staticmethod
    def searchOffer(profile):
        return WantedCategory.objects.filter(profile=profile, type_category=2)

    def updateHave(profile, oldcategory, category):
        WantedCategory.objects.filter(profile=profile, type_category=1, category=oldcategory).delete()
        return WantedCategory.create(category.id, profile, 1)

    def updateOffer(profile, oldcategory, category):
        WantedCategory.objects.filter(profile=profile, type_category=2, category=oldcategory).delete()
        return WantedCategory.create(category.id, profile, 2)


class Label(models.Model):
    name = models.CharField(max_length=100)


class SuggestedCategory(models.Model):
    category = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return '%s %s' % (self.category, self.profile)

    def create(element, profile):
        suggested = SuggestedCategory(profile=profile, category=str(element))
        return suggested.save()
