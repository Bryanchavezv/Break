from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True, db_column='idrol')
    rol = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.rol

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True, db_column='idgenero')
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.genero

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=128, default='defaultpassword')
    telefono = models.CharField(max_length=45)
    
    def __str__(self):
        return self.email

    


class MensajeForo(models.Model):
    id_mensaje          = models.AutoField(primary_key=True)
    autor               = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido           = models.TextField()
    fecha_publicacion   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje por {self.autor} el {self.fecha_publicacion}"

class Libro(models.Model):
    id_libro   = models.CharField(primary_key=True, max_length=13)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titulo

class CompraLibro(models.Model):
    id_compra       = models.AutoField(primary_key=True)
    libro           = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad        = models.PositiveIntegerField()
    fecha_compra    = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Compra de {self.cantidad} unidades de {self.libro.titulo} el {self.fecha_compra}"




