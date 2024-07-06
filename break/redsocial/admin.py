from django.contrib import admin
from .models import Usuario, Rol, Genero, Libro,CompraLibro,MensajeForo

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'email', 'fecha_nacimiento', 'id_rol', 'id_genero','password')
    search_fields = ('rut', 'nombre', 'apellido_paterno', 'email')
    list_filter = ('activo', 'id_rol', 'id_genero')

admin.site.register(Usuario, )
admin.site.register(Rol)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(CompraLibro)
admin.site.register(MensajeForo)