from django.db import models
from profiles.models import Profile, File
from django.shortcuts import get_object_or_404


class Category(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=28)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to=File.generatePath, default='Category/no.image.png')
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

    def getSubCategories(category):
        return Category.objects.filter(pattern=category).order_by('name')


class WantedCategory(models.Model):
    category = models.ForeignKey(Category)
    profile = models.ForeignKey(Profile)
    # i_have(Ofrezco) --> 1 ; i_search(Busco) --> 2
    type_category = models.IntegerField()

    def __str__(self):
        return str(self.category)

    def create(element, profile, kind):
        category = get_object_or_404(Category, id=element)
        wanted = WantedCategory(profile=profile, category=category, type_category=kind)
        return wanted.save()

    def deleteAllHave(profile):
        WantedCategory.objects.filter(profile=profile, type_category=1).delete()

    def deleteAllSearch(profile):
        WantedCategory.objects.filter(profile=profile, type_category=2).delete()

    def searchOffer(profile):
        return WantedCategory.objects.filter(profile=profile, type_category=2)

    def searchHave(profile):
        return WantedCategory.objects.filter(profile=profile, type_category=1)


class SuggestedCategory(models.Model):
    category = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return '%s %s' % (self.category, self.profile)

    def create(element, profile):
        suggested = SuggestedCategory(profile=profile, category=str(element))
        return suggested.save()
