from django.contrib import admin
from django.urls import path, include
from setup import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('materiais/', include('material.urls')),
    path('movimentacao/', include('movimentacao.urls')),
    path('producao/', include('producao.urls')),
    path('roupas/', include('roupa.urls')),
    path('usuario/', include('usuario.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
