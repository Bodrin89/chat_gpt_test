from django.urls import path

from apps.chat.views import ChatRequestView

urlpatterns = [
    path('requests', ChatRequestView.as_view(), name='chat_request'),
]