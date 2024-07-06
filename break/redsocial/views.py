from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .forms import RegistrarForm, LoginForm, LibroForm
from .models import Usuario, Libro

def index(request):
    return render(request, 'redsocial/index.html')

def contraseña(request):
    return render(request, 'redsocial/contraseña.html')

def editar_perfil(request):
    return render(request, 'redsocial/editar_perfil.html')

def marketplace(request):
    libros = Libro.objects.all()
    return render(request, 'redsocial/marketplace.html', {'libros': libros})

def carro(request):
    return render(request, 'redsocial/carro.html')

def registrar(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data['password'])
            usuario.save()
            messages.success(request, 'Cuenta creada con éxito')
            return redirect('login')
    else:
        form = RegistrarForm()
    return render(request, 'redsocial/registrar.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                usuario = Usuario.objects.get(email=email)
                if check_password(password, usuario.password):
                    request.session['usuario_id'] = usuario.rut  # Guardar el ID del usuario en la sesión
                    return redirect('inicio')
                else:
                    messages.error(request, 'Correo electrónico o contraseña incorrectos')
            except Usuario.DoesNotExist:
                messages.error(request, 'Correo electrónico o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'redsocial/login.html', {'form': form})

def inicio(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.get(rut=usuario_id)
        return render(request, 'redsocial/inicio.html', {'usuario': usuario})
    else:
        return redirect('login')

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketplace')  # Redirige de vuelta a la página del marketplace
    else:
        form = LibroForm()
    return render(request, 'redsocial/marketplace.html', {'form': form})


