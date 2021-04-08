from django.urls import path,include
from .views import UserCreate, UserUpdate
from rest_framework import routers
from .api.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'usuario', UserViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('cadastro/', UserCreate.as_view(), name="userCreate"),
    path('editar/<int:pk>/', UserUpdate.as_view(), name="userUpdate"),
]
