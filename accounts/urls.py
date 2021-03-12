from django.urls import path
from .views import Login, UserCreate, Password

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('cadastro/', UserCreate.as_view(), name="userCreate"),
    path('password/', Password.as_view(), name="password"),
]