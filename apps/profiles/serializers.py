from rest_framework.serializers import ModelSerializer

from apps.profiles.models import MyProfile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = MyProfile
        fields = ('id', 'user', 'location', 'my_group', 'my_event')


class ProfileDetailSerializer(ModelSerializer):
    class Meta:
        model = MyProfile
        fields = ('id', 'user', 'location', 'my_group', 'my_event')