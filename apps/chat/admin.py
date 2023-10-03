from django.contrib import admin

from apps.chat.models import ChatModel


@admin.register(ChatModel)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('text', 'answer')
    search_fields = ('text',)
    search_help_text = 'Поиск по тексту запроса'
