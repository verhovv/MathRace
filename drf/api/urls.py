from django.urls import path

from .views import *

urlpatterns = [
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('answer/', answer_view, name='answer'),
    path('task/', get_task, name='task'),
    path('enemy/', enemy_view, name='enemy'),
    path('room/', RoomView.as_view(), name='room'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('change-username/', change_username_view, name='change_username'),
    path('change-password/', change_password_view, name='change_password')
]
