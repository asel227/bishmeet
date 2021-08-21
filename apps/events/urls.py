from django.urls import path

from apps.events.views import (EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView, EventListViewSet)

urlpatterns = [
    path('events/',
         EventListCreateAPIView.as_view(), name='api_event_list'),
    path('event/<int:pk>',
         EventRetrieveUpdateDestroyAPIView.as_view(), name='api_event_detail'),
    path('timestamp/',
         EventListViewSet, name='api_event_datetime'),
]
