from django.shortcuts import render, redirect
from .forms import contato



def main(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicial.html')

def login(request):
    return render(request, 'login.html')

def cadastroOng(request):

    return render(request, 'cadastroOng.html')

def cadastroUser(request):

    return render(request, 'cadastrouser.html')

def perfil(request):

    return render(request, 'perfil.html')

def infos(request):

    return render(request, 'infos.html')

def favoritos(request):

    return render(request, 'favoritos.html')


