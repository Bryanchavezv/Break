from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario, Rol, Genero

class RegistroUsuarioForm(UserCreationForm):
    rut = forms.CharField(label='RUT', max_length=10)
    nombre = forms.CharField(label='Nombre', max_length=20)
    apellido_paterno = forms.CharField(label='Apellido Paterno', max_length=20)
    apellido_materno = forms.CharField(label='Apellido Materno', max_length=20)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))
    id_rol = forms.ModelChoiceField(queryset=Rol.objects.all(), label='Rol')
    id_genero = forms.ModelChoiceField(queryset=Genero.objects.all(), label='Género')
    telefono = forms.CharField(label='Teléfono', max_length=45)
    email = forms.EmailField(label='Email', max_length=100, required=False)
    direccion = forms.CharField(label='Dirección', max_length=50, required=False)
    activo = forms.BooleanField(label='Activo', required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'id_rol', 'id_genero', 'telefono', 'email', 'direccion', 'activo']



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario', max_length=150)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
