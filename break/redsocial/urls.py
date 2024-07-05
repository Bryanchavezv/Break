from django.urls import path
from . import views  # Importa las vistas

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para el index
    path('contraseña/', views.contraseña, name='contraseña'),  # Ruta para cambiar contraseña
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),  # Ruta para cambiar editar_perfil
    path('inicio/', views.inicio, name='inicio'),  # Ruta para cambiar inicio
    path('login/', views.login, name='login'),  # Ruta para cambiar login
    path('registrar/', views.registrar, name='registrar'),  # Ruta para registrar
]
