from rest_framework.generics import RetrieveAPIView, CreateAPIView
from apps.chat.serializers import ChatRequestSerializer
from rest_framework.response import Response

from apps.chat.models import ChatModel
from apps.chat.services import ChatRequestService


class ChatRequestView(CreateAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ChatRequestSerializer

    def create(self, request, *args, **kwargs):

        answer = ChatRequestService.request(request.data['text'])
        serializer = self.serializer_class(answer)
        return Response(serializer.data)

        # return Response(answer)




