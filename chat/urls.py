from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_chat, name='chat_index'),
    path('<str:room_name>/', views.room, name='room'),
]