from django.contrib import admin

# Register your models here.
from .models import Follow, Profile, Place, Icon
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# admin.site.register(Album)


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'email', 'get_full_name', 'location', 'last_login', 'date_joined')

    list_filter = (
        ('user__date_joined', DateRangeFilter), ('user__last_login', DateTimeRangeFilter),
    )

    def date_joined(self, obj):
        return obj.user.date_joined
    date_joined.short_description = 'Date join'
    date_joined.admin_order_field = 'user__date_joined'

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    def email(self, obj):
        return obj.user.email

    def last_login(self, obj):
        return obj.user.last_login
    last_login.short_description = 'Last login'
    last_login.admin_order_field = 'user__last_login'


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('name', 'pattern')


@admin.register(Follow)
class AdminFollow(admin.ModelAdmin):
    list_display = ('following', 'follower')


@admin.register(Icon)
class AdminIcon(admin.ModelAdmin):
    list_display = ('name',)
