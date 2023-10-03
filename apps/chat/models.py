from django.db import models


class ChatModel(models.Model):
    """Модель запроса к chat gpt"""

    text = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
