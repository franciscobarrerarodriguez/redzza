from django.contrib import admin

# Register your models here.

from .models import Commentary, Video, Image, CityNotice, Notice, Color, Product, Service
from rangefilter.filter import DateRangeFilter
# from sorl.thumbnail import get_thumbnail


@admin.register(Notice)
class AdminNotice(admin.ModelAdmin):
    list_display = ('title', 'category', 'profile', 'location', 'get_kind', 'visibility', 'urgency', 'date')
    list_filter = (('date', DateRangeFilter), 'visibility', 'kind', 'urgency')
    ordering = ('-date',)

    def get_kind(self, obj):
        return "%s" % ("i_have" if obj.kind == 1 else "i_search")
    get_kind.short_description = 'Kind'
    get_kind.admin_order_field = 'kind'


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
