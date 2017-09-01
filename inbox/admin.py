from django.contrib import admin
from .models import Conversation, Message


# Register your models here.
@admin.register(Conversation)
class AdminConversation(admin.ModelAdmin):
    list_display = ('modified',)


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ('contestant', 'text')
