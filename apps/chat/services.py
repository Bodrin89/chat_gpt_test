import os
import openai
from dotenv import load_dotenv

from apps.chat.models import ChatModel

load_dotenv()

openai.api_key = os.getenv('API_KEY_OPENAI')


class ChatRequestService:

    @staticmethod
    def request(request_text):
        # response = openai.Completion.create(
        #     engine="ada-code-search-text",
        #     prompt=request_text,
        #     max_tokens=50
        # )
        # return response
        response = ChatModel.objects.create(text=request_text, answer="ответ на вопрос: {request_text}")
        return response

