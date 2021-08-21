import json

import django_filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.events.models import Event
from apps.events.serializers import EventDetailSerializer, EventSerializer


class EventFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(name="timestamp", lookup_expr='gte')

    class Meta:
        model = Event
        fields = ['event_date', 'event_time', 'timestamp', 'timestamp_gte']


class EventListViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_class = EventFilter
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['=name', 'event_date', 'event_time']


class EventListCreateAPIView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def filter_queryset(self, queryset):
        queryset = super(EventListCreateAPIView, self).filter_queryset(queryset)
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name_icontains=name)

        return queryset


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EventDetailSerializer
