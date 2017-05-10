from django.contrib import admin

# Register your models here.

from .models import Notice, Color, Product, Service


@admin.register(Notice)
class AdminNotice(admin.ModelAdmin):
    list_display = ('title', 'optionTrade')


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('notice', 'quantity')


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    list_display = ('hexa', 'product')


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('notice', 'time')
