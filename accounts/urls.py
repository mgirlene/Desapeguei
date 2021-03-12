from django.urls import path
from .views import Login, Register, Password

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('cadastro/', Register.as_view(), name="register"),
    path('password/', Password.as_view(), name="password"),
]