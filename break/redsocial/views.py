from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .forms import RegistrarForm, LoginForm,PublicarMensajeForm, ResponderMensajeForm
from .models import Usuario,MensajeForo

def index(request):
    return render(request, 'redsocial/index.html')

def contraseña(request):
    return render(request, 'redsocial/contraseña.html')


def editar_perfil(request):
    return render(request, 'redsocial/editar_perfil.html')




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
    if not usuario_id:
        return redirect('login')
    
    usuario = Usuario.objects.get(rut=usuario_id)
    
    if request.method == 'POST':
        if 'publicar' in request.POST:
            form = PublicarMensajeForm(request.POST)
            if form.is_valid():
                mensaje = form.save(commit=False)
                mensaje.autor = usuario
                mensaje.save()
                messages.success(request, 'Mensaje publicado con éxito')
                return redirect('inicio')
        elif 'responder' in request.POST:
            mensaje_id = request.POST.get('mensaje_id')
            mensaje_padre = MensajeForo.objects.get(id_mensaje=mensaje_id)
            form = ResponderMensajeForm(request.POST)
            if form.is_valid():
                respuesta = form.save(commit=False)
                respuesta.autor = usuario
                respuesta.mensaje_padre = mensaje_padre
                respuesta.save()
                messages.success(request, 'Respuesta publicada con éxito')
                return redirect('inicio')
    else:
        form = PublicarMensajeForm()
        respuesta_form = ResponderMensajeForm()
    
    mensajes = MensajeForo.objects.filter(mensaje_padre__isnull=True).order_by('-fecha_publicacion')
    
    return render(request, 'redsocial/inicio.html', {
        'usuario': usuario,
        'form': form,
        'respuesta_form': respuesta_form,
        'mensajes': mensajes
    })
