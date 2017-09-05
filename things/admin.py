from django.contrib import admin

# Register your models here.

from .models import Commentary, Video, Image, CityNotice, Notice, Color, Product, Service
from sorl.thumbnail import get_thumbnail


@admin.register(Notice)
class AdminNotice(admin.ModelAdmin):
    list_display = ('title', 'category')


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('notice', 'state')


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    list_display = ('hexa', 'product')


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('notice', 'time')


@admin.register(CityNotice)
class AdminCityNotice(admin.ModelAdmin):
    list_display = ('city', 'notice')


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    #    def image_notice(self, obj):
    #        print(obj.image.url)
    #        return '<img src ="%s">' % get_thumbnail(obj.image, '100x100').url
    #    image_notice.allow_tags = True
    list_display = ('notice',)


@admin.register(Video)
class AdminVideo(admin.ModelAdmin):
    list_display = ('notice',)


@admin.register(Commentary)
class AdminCommentary(admin.ModelAdmin):
    list_display = ('commentary', 'profile', 'notice')
