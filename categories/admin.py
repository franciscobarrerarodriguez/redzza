from django.contrib import admin

# Register your models here.
from .models import Category, WantedCategory, SuggestedCategory


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('pattern', 'name')


@admin.register(WantedCategory)
class AdminWantedCategory(admin.ModelAdmin):
    list_display = ('category', 'profile', 'type_category')


@admin.register(SuggestedCategory)
class AdminSuggestedCategory(admin.ModelAdmin):
    list_display = ('category', 'profile')
