from django.urls import path

from apps.groups.views import GroupListCreateAPIView, GroupRetrieveUpdateDestroyAPIView, RatingListAPIView


urlpatterns = [
    path('groups/',
         GroupListCreateAPIView.as_view(), name='api_group_list'),
    path('group/<int:pk>',
         GroupRetrieveUpdateDestroyAPIView.as_view(),
         name='api_group_detail'),
    path('rating/',
         RatingListAPIView.as_view(), name='api_rating_list'),
]