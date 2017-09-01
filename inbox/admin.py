from django.contrib import admin
from .models import Conversation, Message


# Register your models here.
@admin.register(Conversation)
class AdminProfile(admin.ModelAdmin):
    list_display = ('modified',)


@admin.register(Message)
class AdminPlace(admin.ModelAdmin):
    list_display = ('user', 'text')
