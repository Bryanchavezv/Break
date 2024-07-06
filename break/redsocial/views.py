from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm,LoginForm



def index(request):

    return render(request, 'redsocial/index.html')

def login(request):
    return render(request, 'redsocial/login.html')


def contraseña(request):
    return render(request, 'redsocial/contraseña.html')

def inicio(request):
    return render(request, 'redsocial/inicio.html')


def registrar(request):
    return render(request, 'redsocial/registrar.html')

def editar_perfil(request):
    return render(request, 'redsocial/editar_perfil.html')



def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # Redirigir al usuario a la página deseada después del registro
            return redirect('redsocial/inicio.html')  # Cambia 'pagina_principal' por la URL a la que deseas redirigir
    else:
        form = RegistroUsuarioForm()
    return render(request, 'redsocial/registro.html', {'form': form})



def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir al usuario a la página deseada después del inicio de sesión
                return redirect('redsocial/inicio.html')  # Cambia 'pagina_principal' por la URL a la que deseas redirigir
            else:
                # Manejar el caso cuando las credenciales no son válidas
                # Por ejemplo, mostrar un mensaje de error
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    
    return render(request, 'redsocial/login.html', {'form': form})
