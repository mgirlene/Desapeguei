from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title=' API`s Desapeguei ')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('', include('gerenciador.urls')),
    path('favorito/', include('favorito.urls')),
    path('anuncio/', include('anuncio.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
