from django.urls import path

from apps.events.views import (EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView,
                               comments_list, comment_detail, EventListViewSet, EventDetailView)

urlpatterns = [
    path('events/',
         EventListCreateAPIView.as_view(), name='api_event_list'),
    path('event/<int:pk>',
         EventRetrieveUpdateDestroyAPIView.as_view(),
         name='api_event_detail'),
    path('comments/', comments_list, name='comments_list'),
    path('comments/<int:pk>', comment_detail, name='comment_detail'),
    path('event_datetime/',
         EventListViewSet, name='api_event_datetime'),

]
