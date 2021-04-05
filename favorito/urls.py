from django.urls import path
from .views import *

urlpatterns = [
    path('favorito/adicionar/', FavoritoView.as_view(), name="add_favorito"),
    path('favorito/deletar/<int:pk>/', deleteFavoritas, name="del_favorito"),
    path('favorito/listar/', listFavoritas, name="list_favorito"),
]