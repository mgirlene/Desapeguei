from django.urls import path, include
from .views import *
from rest_framework import routers
from .api.viewsets import AnuncioViewSet

router = routers.DefaultRouter()
router.register(r'favorito', AnuncioViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('adicionar/', FavoritoView.as_view(), name="add_favorito"),
    path('deletar/<int:pk>/', deleteFavoritas, name="del_favorito"),
    path('listar/', listFavoritas, name="list_favorito"),
]