from django.urls import path #llamar urls django y la ruta con el path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista de índice (index es de views)
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),


]