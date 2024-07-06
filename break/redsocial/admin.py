from django.contrib import admin
from .models import Usuario, Rol, MensajeForo, Libro, CompraLibro, Genero

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono')
    search_fields = ('rut', 'nombre', 'apellido_paterno', 'email', 'telefono')

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'rol')
    search_fields = ('rol',)

@admin.register(MensajeForo)
class MensajeForoAdmin(admin.ModelAdmin):
    list_display = ('id_mensaje', 'autor', 'contenido', 'fecha_publicacion')
    search_fields = ('autor__nombre', 'contenido', 'fecha_publicacion')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titulo', 'autor', 'editorial', 'precio')
    search_fields = ('isbn', 'titulo', 'autor')

@admin.register(CompraLibro)
class CompraLibroAdmin(admin.ModelAdmin):
    list_display = ('id_compra', 'libro', 'cantidad', 'fecha_compra')
    search_fields = ('libro__titulo', 'fecha_compra')