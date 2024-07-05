from django.shortcuts import render

def index(request):

    return render(request, 'redsocial/index.html')

def contraseña(request):
    return render(request, 'redsocial/contraseña.html')

def editar_perfil(request):
    return render(request, 'redsocial/editar_perfil.html')

def inicio(request):
    return render(request, 'redsocial/inicio.html')

def login(request):
    return render(request, 'redsocial/login.html')

def registrar(request):
    return render(request, 'redsocial/registrar.html')
