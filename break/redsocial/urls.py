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
    path('carro/', views.carro_view, name='carro'),


    path('agregar_libro', views.agregar_libro, name='agregar_libro'),
    path('eliminar_libro/<int:id_libro>/', views.eliminar_libro, name='eliminar_libro'),
    path('editar_libro/<int:id_libro>/', views.editar_libro, name='editar_libro'),

    path('agregar_al_carrito/<int:libro_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:libro_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar-carrito/', views.vaciar_carrito, name='vaciar_carrito'),
]
