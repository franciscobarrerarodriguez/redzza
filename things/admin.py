from django.contrib import admin

# Register your models here.

from .models import Notice, Color


@admin.register(Notice)
class AdminNotice(admin.ModelAdmin):
    list_display = ('title', 'optionTrade')


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    list_display = ('name', 'notice')
