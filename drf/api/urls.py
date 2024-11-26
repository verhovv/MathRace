from django.urls import path

from .views import *

urlpatterns = [
    path('leaderboard/', leaderboard_view),
    path('task/', get_task),
    path('answer/', answer_view),
    path('enemy/', enemy_view),
    path('room/', RoomView.as_view()),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
