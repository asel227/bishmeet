from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.profiles.models import MyProfile
from apps.users.models import User


class MyProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'age', 'gender', 'avatar')


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = MyProfile
        fields = ('id', 'profile', 'location', 'my_group', 'my_event')


class ProfileDetailSerializer(ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        source='profile',
        queryset=User.objects.all(),
    )
    profile = MyProfileSerializer(read_only=False)

    class Meta:
        model = MyProfile
        fields = ('id', 'profile_id', 'profile', 'location', 'my_group', 'my_event')