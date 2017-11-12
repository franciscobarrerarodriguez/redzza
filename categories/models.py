from django.db import models
from profiles.models import Profile, File
from django.shortcuts import get_object_or_404


class Category(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to=File.generatePath, default='Category/no.image.png')
    color = models.CharField(max_length=7, default="#FFFFFF")

    def __str__(self):
        return self.name

    def getSubCategories(category):
        return Category.objects.filter(pattern=category).order_by('name')


class WantedCategory(models.Model):
    category = models.ForeignKey(Category)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return str(self.category)

    def create(element, profile):
        category = get_object_or_404(Category, id=element)
        wanted = WantedCategory(profile=profile, category=category)
        return wanted.save()

    def deleteAll(profile):
        WantedCategory.objects.filter(profile=profile).delete()

    def search(profile):
        return WantedCategory.objects.filter(profile=profile)


class SuggestedCategory(models.Model):
    category = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return '%s %s' % (self.category, self.profile)

    def create(element, profile):
        suggested = SuggestedCategory(profile=profile, category=str(element))
        return suggested.save()
