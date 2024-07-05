
from django.contrib import admin
from django.urls import path, include #(include)redirecciona al urls.py de alumnos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('redsocial.urls')),#redirecciona al urls.py de alumnos(cuando no haya nada '' muestra 'alumnos.urls')
]

