import json

from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from apps.groups.models import Group, Rating
from apps.groups.serializers import GroupSerializer, GroupDetailSerializer, RatingSerializer


class GroupListCreateAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_group_fields = ['=name']

    def filter_queryset(self, queryset):
        queryset = super(GroupListCreateAPIView, self).filter_queryset(queryset)
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name_icontains=name)

        return queryset


class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GroupDetailSerializer


class RatingListAPIView(ListCreateAPIView):
    queryset = Rating.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer
