from django.urls import path, include
from .views import AnuncioView,AnuncioUpdateView,AnuncioDeleteView,AnuncioListView, AnuncioDetailsView,ContactForm
from rest_framework import routers
from .api.viewsets import AnuncioViewSet

router = routers.DefaultRouter()
router.register(r'anuncio', AnuncioViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('cadastrar/', AnuncioView.as_view(), name="anuncio_cadastro"),
    path('listar/', AnuncioListView.as_view(), name='anuncio_lista'),
    path('editar/<int:pk>', AnuncioUpdateView.as_view(), name='anuncio_editar'),
    path('deletar/<int:pk>/', AnuncioDeleteView.as_view(), name='anuncio_delete'),
    path('detalhar/<int:pk>/', AnuncioDetailsView.as_view(), name='anuncio_details'),
    path('contact/', ContactForm.as_view(), name='contact'),
]
