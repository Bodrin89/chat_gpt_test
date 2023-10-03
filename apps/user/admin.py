from django.contrib import admin

from apps.chat.models import ChatModel
from apps.user.models import User


@admin.register(User)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username',)
    search_help_text = 'Поиск по имени юзера'

