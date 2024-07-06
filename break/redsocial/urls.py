from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login', views.login_view, name='login'),  # Cambiado a 'login/' para corresponder con la URL esperada
    path('registrar', views.registrar, name='registrar'), 
    path('inicio', views.inicio, name='inicio'), 
    path('editar_perfil', views.editar_perfil, name='editar_perfil'), 
    path('contraseña', views.contraseña, name='contraseña'), 
    path('marketplace', views.marketplace, name='marketplace'), 
    path('carro', views.carro, name='carro'), 
]