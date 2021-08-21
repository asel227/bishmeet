from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.validators import UniqueValidator

from apps.users.models import User
from core import settings


class AuthSerializer(Serializer):
    email = serializers.EmailField(max_length=60)
    password = serializers.CharField(max_length=128)

#
# class PasswordSerializer (PasswordResetSerializer):
#     password_reset_form_class = ResetPasswordForm


class UsersListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'age', 'gender', 'email', 'is_active'
        )


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'age', 'gender', 'get_avatar', 'email',
        )


class RegisterSerializer(ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', 'gender', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    def email_user(self, subject, message, from_email=settings.DEFAULT_FROM_EMAIL, **kwargs):
        send_mail(subject, message, from_email, [self.email], fail_silently=False, **kwargs)