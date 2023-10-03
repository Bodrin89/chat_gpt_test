
from rest_framework import serializers

from apps.chat.models import ChatModel


class ChatRequestSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    answer = serializers.CharField(read_only=True,)

    class Meta:
        model = ChatModel
        fields = '__all__'
