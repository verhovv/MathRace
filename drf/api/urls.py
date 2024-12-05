from django.urls import path

from .views import *
from .views import register_view, login_view, profile_view

urlpatterns = [
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('answer/', answer_view, name='answer'),
    path('task/', get_task, name='task'),
    path('enemy/', enemy_view, name='enemy'),
    path('room/', room_view, name='room'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
]
