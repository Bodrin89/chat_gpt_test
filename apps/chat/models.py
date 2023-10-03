from django.db import models
from django.db.models import CASCADE

from apps.user.models import User


class ChatModel(models.Model):
    """Модель запроса к chat gpt"""

    text = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
