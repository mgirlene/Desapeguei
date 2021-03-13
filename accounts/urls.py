from django.urls import path
from .views import UserCreate,UserUpdate

urlpatterns = [
    path('cadastro/', UserCreate.as_view(), name="userCreate"),
    path('editar/<int:pk>/', UserUpdate.as_view(), name="userUpdate"),
]
