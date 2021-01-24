from rest_framework import serializers

from chats import models


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Chat
        fields = ('started', 'users')