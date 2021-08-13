from django.urls import path

from apps.events.views import EventCreateAPIView, EventRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('events/',
         EventCreateAPIView.as_view(), name='api_event_list'),
    path('event/<int:pk>',
         EventRetrieveUpdateDestroyAPIView.as_view(),
         name='api_event_detail'),
]