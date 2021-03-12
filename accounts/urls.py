from django.urls import path
from .views import UserCreate

urlpatterns = [
    path('cadastro/', UserCreate.as_view(), name="userCreate"),
]