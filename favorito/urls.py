from django.urls import path
from .views import *

urlpatterns = [
    path('adicionar/', FavoritoView.as_view(), name="add_favorito"),
    path('deletar/<int:pk>/', deleteFavoritas, name="del_favorito"),
    path('listar/', listFavoritas, name="list_favorito"),
]