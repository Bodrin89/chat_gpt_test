from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.chat.models import ChatModel
from apps.chat.serializers import ChatRequestSerializer
from apps.chat.services import ChatRequestService


class ChatRequestView(CreateAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ChatRequestSerializer

    def create(self, request, *args, **kwargs):
        print(request)

        answer = ChatRequestService.request(request)
        serializer = self.serializer_class(answer)
        return Response(serializer.data)
