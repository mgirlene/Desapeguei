from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('', include('gerenciador.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('pagamento/', include('pagamento.urls')),
    path('produto/', include('produto.urls')),
    path('vendas/', include('vendas.urls')),

]
