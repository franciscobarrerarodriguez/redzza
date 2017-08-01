# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tag, TagProfile


# Register your models here.
@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TagProfile)
class AdminTagProfile(admin.ModelAdmin):
    list_display = ('tag', 'profile')
