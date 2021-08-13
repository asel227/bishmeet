from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)
from django.core.mail import send_mail

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.serializers import AuthSerializer, UsersListSerializer, UsersCreateSerializer, UserDetailSerializer, \
    RegisterSerializer


class UserAuthView(APIView):
    permission_classes = [AllowAny]
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.data.get('email')).first()

        if user is None:
            return Response(
                data={'error': 'Пользователь не найден'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not user.check_password(serializer.data.get('password')):
            return Response(
                data={'error': 'Не верный пароль'},
                status=status.HTTP_404_NOT_FOUND,
            )

        user_token, created = Token.objects.get_or_create(user=user)

        return Response(data={'token': user_token.key}, status=status.HTTP_200_OK)


class UsersListAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        self.serializer_class = UsersListSerializer
        return super(UsersListAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = UsersCreateSerializer
        return super(UsersListAPIView, self).post(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(serializer.validated_data.get('password'))
        instance.save()

    # def perform_create(self, serializer):
    #     created_object = serializer.save()
    #     send_mail('Subject here', 'Here is the message.', 'from@example.com',
    #         [created_object.email],  fail_silently=False,)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(serializer.validated_data.get('password'))
        instance.save()

