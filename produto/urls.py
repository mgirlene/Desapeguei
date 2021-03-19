from django.urls import path
from .views import ProdutoView,ProdutoUpdateView,ProdutoDeleteView,ProdutoListView

urlpatterns = [
    path('cadastrar/', ProdutoView.as_view(), name="produto_cadastro"),
    path('listar/', ProdutoListView.as_view(), name='produto_list'),
    path('editar/<int:pk>', ProdutoUpdateView.as_view(), name='produto_editar'),
    path('deletar/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),

]
