from django.urls import path
from .views import AnuncioView,AnuncioUpdateView,AnuncioDeleteView,AnuncioListView

urlpatterns = [
    path('cadastrar/', AnuncioView.as_view(), name="anuncio_cadastro"),
    path('listar/', AnuncioListView.as_view(), name='anuncio_lista'),
    path('editar/<int:pk>', AnuncioUpdateView.as_view(), name='anuncio_editar'),
    path('deletar/<int:pk>/', AnuncioDeleteView.as_view(), name='anuncio_delete'),

]
