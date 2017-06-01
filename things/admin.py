from django.contrib import admin

# Register your models here.

from .models import Commentary, Video, Image, CategoryTrade, CityNotice, Notice, Color, Product, Service


@admin.register(Notice)
class AdminNotice(admin.ModelAdmin):
    list_display = ('title', 'category')


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('notice', 'quantity')


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    list_display = ('hexa', 'product')


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('notice', 'time')


@admin.register(CityNotice)
class AdminCityNotice(admin.ModelAdmin):
    list_display = ('city', 'notice')


@admin.register(CategoryTrade)
class AdminCategoryTrade(admin.ModelAdmin):
    list_display = ('category', 'notice')


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ('notice',)


@admin.register(Video)
class AdminVideo(admin.ModelAdmin):
    list_display = ('notice',)


@admin.register(Commentary)
class AdminCommentary(admin.ModelAdmin):
    list_display = ('commentary', 'profile', 'notice')
