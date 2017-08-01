from django.contrib import admin

# Register your models here.
from .models import Follow, Profile, Place

# admin.site.register(Album)


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'location')


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('name', 'pattern')


@admin.register(Follow)
class AdminFollow(admin.ModelAdmin):
    list_display = ('following', 'follower')
