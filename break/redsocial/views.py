from django.shortcuts import render

def index(request):

    return render(request, 'redsocial/index.html')

def login(request):
    return render(request, 'redsocial/login.html')