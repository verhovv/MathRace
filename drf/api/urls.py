from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('leaderboard/', leaderboard_view),
    path('task/', get_task),
    path('answer/', answer_view),
    path('enemy/', enemy_view),
    path('room/', RoomView.as_view())
]