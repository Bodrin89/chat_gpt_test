from typing import Callable

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed

from apps.user.models import User
from apps.user.serializers import CreateUserSerializer
from rest_framework.request import Request


class UserServices:

    @staticmethod
    def signup_user(user_data: CreateUserSerializer) -> User:
        """Создание нового пользователя и сохранение его в БД с захэшированным паролем"""
        del user_data.validated_data['password_repeat']
        user_data.validated_data['password'] = make_password(user_data.validated_data['password'])
        user = User.objects.create(**user_data.validated_data)
        return user

    @staticmethod
    def login_user(user_data: Request, serializer_data: Callable) -> User:
        """Аутентификация пользователя"""
        if not (user := authenticate(
                username=user_data.data.get('username', None),
                password=user_data.data.get('password', None)
        )):
            raise AuthenticationFailed
        else:
            serializer = serializer_data(data={'username': user.username,
                                               'password': user.password})
            serializer.is_valid(raise_exception=True)
            return user
