from django.contrib.auth import login, logout
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers import CreateUserSerializer, LoginSerializer
from apps.user.services import UserServices


class SignUpView(CreateAPIView):
    """Регистрация пользователя"""
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs) -> Response:
        """Создание нового пользователя и сохранение его в БД с захэшированным паролем"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserServices.signup_user(serializer)
        return Response(data={'id': user.pk, 'username': user.username, 'first_name': user.first_name})


class LoginView(CreateAPIView):
    """Вход в учетную запись"""
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer
        user = UserServices.login_user(request, serializer)
        login(request=request, user=user)
        return Response(data={'id': user.pk, 'username': user.username, 'first_name': user.first_name})


class LogoutView(APIView):
    """Выход из учетной записи"""

    def post(self, request) -> Response:
        logout(request)
        return Response({'detail': 'Logged out successfully.'})
