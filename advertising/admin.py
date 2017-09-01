from django.contrib import admin

from .models import Advertising
# Register your models here.


@admin.register(Advertising)
class AdminAdvertising(admin.ModelAdmin):
    list_display = ('title',)
