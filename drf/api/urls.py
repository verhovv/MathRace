from django.urls import path

from .views import *

urlpatterns = [
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('answer/', answer_view, name='answer'),
    path('enemy/', enemy_view, name='enemy'),
    path('room/', room_view, name='room'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
