from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login', views.login, name='login'), 
    path('registrar', views.registrar, name='registrar'), 
    path('inicio', views.inicio, name='inicio'), 
    path('editar_perfil', views.editar_perfil, name='editar_perfil'), 
    path('contraseña', views.contraseña, name='contraseña'), 
   
   


]

