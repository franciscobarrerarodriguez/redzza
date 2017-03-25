from django.contrib import admin

# Register your models here.
from .models import User, Profile

# admin.site.register(Album)


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    list_filter = ('mail',)


@admin.register(Profile)
class AdminUser(admin.ModelAdmin):
    list_display = ('user',)
