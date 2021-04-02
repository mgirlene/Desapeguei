from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('', include('gerenciador.urls')),
    path('favorito/', include('favorito.urls')),
    path('anuncio/', include('anuncio.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
