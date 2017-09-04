from rest_framework import serializers
from .models import Conversation, Message


class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'url', 'modified', 'contestant', 'notice')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'url', 'timestamp', 'text', 'image', 'review', 'sender', 'conversation')
