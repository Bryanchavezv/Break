from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .forms import RegistrarForm, LoginForm, LibroForm
from .models import Usuario, Libro
import logging

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


def eliminar_libro(request, id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)
    libro.delete()
    messages.success(request, 'Libro eliminado con éxito')
    return redirect('marketplace')


def editar_libro(request, id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)
    
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado con éxito')
            return redirect('marketplace')
    else:
        form = LibroForm(instance=libro)
    
    return render(request, 'redsocial/editar_libro.html', {'form': form, 'libro': libro})



def carro_view(request):
    carrito_ids = request.session.get('carrito', [])
    libros = Libro.objects.filter(id_libro__in=carrito_ids)
    total = sum(libro.precio for libro in libros)
    return render(request, 'redsocial/carro.html', {'carrito': libros, 'total': total})


logger = logging.getLogger(__name__)


def agregar_al_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id_libro=libro_id)
    carrito = request.session.get('carrito', [])
    
    if libro_id not in carrito:
        carrito.append(libro_id)
        request.session['carrito'] = carrito
        logger.debug(f'Libro {libro_id} añadido al carrito.')

    return redirect('marketplace')


def eliminar_del_carrito(request, libro_id):
    carrito = request.session.get('carrito', [])
    
    if libro_id in carrito:
        carrito.remove(libro_id)
        request.session['carrito'] = carrito

    return redirect('carro')


def vaciar_carrito(request):
    if request.method == 'POST':
        # Aquí debes obtener el carrito del usuario actual y vaciarlo
        carrito = request.session.get('carrito', [])
        carrito.clear()  # Vaciar el carrito
        request.session['carrito'] = carrito
        messages.success(request, 'Carrito vaciado exitosamente.')
        return redirect('carro')  # Redirigir al carrito
    return redirect('carro')  # Si no es un POST, redirigir al carrito
