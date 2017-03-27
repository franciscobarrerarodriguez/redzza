from django.contrib import admin

# Register your models here.
from .models import Profile, Place

# admin.site.register(Album)


@admin.register(Profile)
class AdminUser(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Place)
class AdminUser(admin.ModelAdmin):
    list_display = ('name','pattern')
