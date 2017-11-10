from django.contrib import admin

# Register your models here.
from .models import Category, WantedCategory, SuggestedCategory


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    def get_color_html(self, obj):
        return """<div style="width: 25px; height: 25px; background: {};"> <div>""".format(obj.color)

    get_color_html.short_description = 'Color'
    get_color_html.allow_tags = True

    list_display = ('pattern', 'name', 'get_color_html')


@admin.register(WantedCategory)
class AdminWantedCategory(admin.ModelAdmin):
    list_display = ('category', 'profile', 'type_category', 'notice')


@admin.register(SuggestedCategory)
class AdminSuggestedCategory(admin.ModelAdmin):
    list_display = ('category', 'profile')
