from typing import Any

from django.shortcuts import render, redirect
from .forms import contato, endereco, formOng, formUser, formPubliDoador, formPubliOng
from .models import Doador, Ong, Publicacao_Ong, Publicacao_Doador, Endereco, Numero_Contato

data = {}

def main(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicial.html')

def login(request):
    return render(request, 'login.html')

def cadastroEndeOng(request):
    form = endereco(request.POST or None, request.FILES or None)
    formCont = contato(request.POST or None, request.FILES or None)
    if form.is_valid() and formCont.is_valid():
        form.save()
        formCont.save()
        return redirect('url_cadOng')
    data['formEndOng'] = form
    data['formCont'] = formCont
    return render(request, 'cadastroEndeOng.html', data)

def cadastroOng(request):
    form = formOng(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_login')
    data['formOng'] = form
    return render(request, 'cadastroOng.html', data)

def cadastroUser(request):
    formU = formUser(request.POST or None, request.FILES or None)
    if formU.is_valid():
        formU.save()
        return redirect('url_login')
    data['formCad'] = formU
    return render(request, 'cadastroUser.html',data)

def cadastroEnde(request):
    form = endereco(request.POST or None, request.FILES or None)
    formCont = contato(request.POST or None, request.FILES or None)
    if form.is_valid() and formCont.is_valid():
        form.save()
        formCont.save()
        return redirect('url_cadUser')
    data['formEnd'] = form
    data['formCont'] = formCont
    return render(request, 'cadastroEnde.html', data)


def perfil(request):

    return render(request, 'perfil.html')

def infos(request):

    return render(request, 'infos.html')

def favoritos(request):

    return render(request, 'favoritos.html')


