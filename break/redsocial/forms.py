from django import forms
from .models import Usuario

class RegistrarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmar_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido_paterno', 'apellido_materno', 'rut', 'fecha_nacimiento', 'id_rol', 'id_genero', 'telefono', 'password']

    def clean_confirmar_password(self):
        password = self.cleaned_data.get('password')
        confirmar_password = self.cleaned_data.get('confirmar_password')
        if password and confirmar_password and password != confirmar_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return confirmar_password

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
