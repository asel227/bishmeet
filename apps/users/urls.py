from django.urls import path

from apps.users.views import UserAuthView, UsersListAPIView, UserRetrieveUpdateDestroyAPIView, RegisterAPIView

urlpatterns = [
    path('auth', UserAuthView.as_view(), name='auth'),
    path('users', UsersListAPIView.as_view(), name='users_list'),
    path('users/<int:pk>',
         UserRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),
    path('register', RegisterAPIView.as_view(), name='register'),
]