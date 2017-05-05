from django.contrib import admin

# Register your models here.
from .models import Profile, Place

# admin.site.register(Album)


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'location')


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('name', 'pattern')
