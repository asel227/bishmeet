from django.urls import path

from apps.profiles.views import ProfileListAPIView, ProfileDetailAPIView

urlpatterns = [
    path('profiles/',
         ProfileListAPIView.as_view(), name='api_profile_list'),
    path('profile/<int:pk>',
         ProfileDetailAPIView.as_view(),
         name='api_profile_detail'),
]