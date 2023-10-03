import os

import openai
from dotenv import load_dotenv

from apps.chat.models import ChatModel

load_dotenv()

openai.api_key = os.getenv('API_KEY_OPENAI')


class ChatRequestService:

    @staticmethod
    def request(request):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=request.data['text'],
            max_tokens=50
        )

        user = request.user
        response = ChatModel.objects.create(user=user,
                                            text=request.data['text'],
                                            answer=response)
        return response

        # user = request.user
        # response = ChatModel.objects.create(user=user,
        #                                     text=request.data['text'],
        #                                     answer=f'ответ на вопрос: {request.data["text"]}')
        # return response
