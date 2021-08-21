from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.profiles.models import MyProfile
from apps.profiles.serializers import ProfileSerializer, ProfileDetailSerializer


class ProfileListAPIView(ListCreateAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = ProfileDetailSerializer
