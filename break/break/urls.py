from django.contrib import admin
from django.urls import path, include  # redirecciona al urls.py de redsocial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('redsocial.urls')),  # Incluye las rutas de la aplicación redsocial
]
