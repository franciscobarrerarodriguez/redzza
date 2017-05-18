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

    def getCategories():
        return Category.objects.filter(pattern__isnull=True).order_by('name')


class WantedCategory(models.Model):
    category = models.ForeignKey(Category)
    profile = models.ForeignKey(Profile)
    # Offer(Ofrezco) --> 1 ; Search(Busco) --> 2
    type_category = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.category, self.profile, self.type_category)

    def create(element, profile, kind):
        category = get_object_or_404(Category, id=element)
        wanted = WantedCategory(profile=profile, category=category, type_category=kind)
        return wanted.save()


class SuggestedCategory(models.Model):
    category = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return '%s %s' % (self.category, self.profile)

    def create(element, profile):
        category = get_object_or_404(Category, id=element)
        suggested = SuggestedCategory(profile=profile, category=category)
        return suggested.save()
