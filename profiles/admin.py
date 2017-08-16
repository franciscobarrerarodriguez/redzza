from django.contrib import admin

# Register your models here.
from .models import Follow, Profile, Place, Icon

# admin.site.register(Album)


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):

    def imagen_admin(self, obj):
        return '<img src="%s" />' % obj.avatar.url

    imagen_admin.allow_tags = True
    readonly_fields = ('imagen_admin',)
    fields = ('user','location','imagen_admin','avatar')
    list_display = ('user', 'location')


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('name', 'pattern')


@admin.register(Follow)
class AdminFollow(admin.ModelAdmin):
    list_display = ('following', 'follower')


@admin.register(Icon)
class AdminIcon(admin.ModelAdmin):
    list_display = ('name',)
