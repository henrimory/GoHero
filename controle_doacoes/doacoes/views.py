from typing import Any

from django.shortcuts import render, redirect
from .forms import contato, endereco, formOng, formUser, formPubliDoador, formPubliOng
from .models import Doador, Ong, Publicacao_Ong, Publicacao_Doador, Endereco, Numero_Contato

data = {}

def home(request):
    return render(request, 'home.html', data)

def homePostOng(request):
    postOngs = Publicacao_Ong.objects.all()
    data['postOngs'] = postOngs
    data['postDoadores'] = False
    return render(request, 'home.html',data)

def homePostDoador(request):
    postDoador = Publicacao_Doador.objects.all()
    data['postOngs'] = False
    data['postDoadores'] = postDoador
    return render(request, 'home.html',data)

def inicio(request):
    return render(request, 'inicial.html')

def logout(request):
    data['acesso'] = False
    data['erroLogin'] = False
    return  render(request, 'login/html', data)

def login(request):
    data['acesso'] = False
    data['erroLogin'] = False
    if request.POST:
        email = request.POST['email']
        senha = request.POST['senha']
        dadoUser = Doador.objects.all()
        dadoOng = Ong.objects.all()

        for dados in dadoUser:
            if dados.email_doador == email and dados.senha == senha:
                data['acesso'] = True
                userLog = Doador.objects.all().get(email_doador=email,senha=senha)
                data['userLog'] = userLog
                data['tipoUser'] = "doador"
                return redirect('url_homePostOng')

        for dadosOng in dadoOng:
            if dadosOng.email_ong == email and dadosOng.senha == senha:
                data['acesso'] = True
                userLog = Ong.objects.all().get(email_ong=email, senha=senha)
                data['userLog'] = userLog
                data['tipoUser'] = "ong"
                return redirect('url_homePostDoador')

        data['erroLogin'] = True
        return render(request, 'login.html', data)

    return render(request, 'login.html')

def contatos(request):
    form = contato(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_cadUser')
    data['formCont'] = form
    return render(request, 'cadastroUser', data)


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
    if data['tipoUser'] == "doador":
        postagens = Publicacao_Doador.objects.filter(id_doador=data['userLog'])
        data['posts'] = postagens
        return render(request, 'perfil.html', data)
    elif data['tipoUser'] == "ong":
        postagens = Publicacao_Ong.objects.filter(id_ong=data['userLog'])
        data['posts'] = postagens
        return render(request, 'perfil.html', data)


def infos(request, pk):
    if data['tipoUser'] == "ong":
        dadosGerais = Ong.objects.get(pk = pk)
        formUpdate = formOng(request.POST or None,request.FILES or None,instance=dadosGerais)
        user = Ong.objects.get(nome=data['userLog'])
    elif data['tipoUser'] == "doador":
        dadosGerais = Doador.objects.get(pk = pk)
        formUpdate = formUser(request.POST or None,request.FILES or None,instance=dadosGerais)
        user = Doador.objects.get(nome=data['userLog'])

    dadosEnde = Endereco.objects.get(logradouro = user.id_endereco)

    formUpdateEnd = endereco(request.POST or None, request.FILES or None, instance=dadosEnde)

    formUpdateCont = contato(request.POST or None, request.FILES or None)
    if formUpdate.is_valid():
        formUpdate.save()
        if data['tipoUser'] == "ong":
            userLog = Ong.objects.all().get(pk=pk)
        elif data['tipoUser'] == "doador":
            userLog = Doador.objects.all().get(pk=pk)
        data['userLog'] = userLog
        return redirect('url_infos',pk)
    if formUpdateEnd.is_valid():
        formUpdateEnd.save()
        return redirect('url_infos', pk)
    if formUpdateCont.is_valid():
        formUpdateCont.save()
        return redirect('url_infos', pk)
    data['formUpdate'] = formUpdate
    data['formUpdateEnd'] = formUpdateEnd
    data['formCont'] = formUpdateCont
    return render(request, 'infos.html', data)

def favoritos(request):

    return render(request, 'favoritos.html',data)


def deletePostOng(request,pk):
    publicacao = Publicacao_Ong.objects.get(pk=pk)
    publicacao.delete()
    return redirect('url_perfil')

def deletePostDoador(request,pk):
    publicacao = Publicacao_Doador.objects.get(pk=pk)
    publicacao.delete()
    return redirect('url_perfil')


def editPostOng(request,pk):

    publicacao = Publicacao_Ong.objects.get(pk=pk)
    form = formPubliOng(request.POST or None, request.FILES or None,instance=publicacao)

    if form.is_valid():
        form.save()
        return redirect('url_perfil')

    data['formEditPostOng'] = form
    return render(request, 'editPostOng.html', data)

def editPostDoador(request,pk):
    publicacao = Publicacao_Doador.objects.get(pk=pk)
    form = formPubliDoador(request.POST or None,request.FILES or None, instance=publicacao)
    if form.is_valid():
        form.save()
        return redirect('url_perfil')
    data['formEditPostDoador'] = form
    return render(request, 'editPostDoador.html', data)


def newPost(request,pk):
    form = formPubliDoador(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_perfil')
    data['formPost'] = form
    return render(request, 'newPost.html', data)


def newPostOng(request,pk):
    form = formPubliOng(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_perfil')
    data['formPost'] = form
    return render(request, 'newPost.html', data)



def visitPerfil(request, pk):
    dadosOng = Ong.objects.all()
    dadosDoa = Doador.objects.all()
    for dado in dadosOng:
        if pk == dado.nome:
            perfilVisitado = Ong.objects.all().get(nome=pk)
            endVisitado = Endereco.objects.get(logradouro = perfilVisitado.id_endereco)
            postagensVisitado = Publicacao_Ong.objects.filter(id_ong=perfilVisitado)
            data['perfilVisitado'] = perfilVisitado
            data['tipoVisitado'] = 'ong'
            data['endVisitado'] = endVisitado
            data['postagensVisitado'] = postagensVisitado
            return render(request, 'visitPerfil.html', data)

    for dado in dadosDoa:
        if pk == dado.nome:
            perfilVisitado = Doador.objects.all().get(nome=pk)
            endVisitado = Endereco.objects.get(logradouro=perfilVisitado.id_endereco)
            postagensVisitado = Publicacao_Doador.objects.filter(id_doador=perfilVisitado)
            data['perfilVisitado'] = perfilVisitado
            data['tipoVisitado'] = 'doador'
            data['endVisitado'] = endVisitado
            data['postagensVisitado'] = postagensVisitado
            return render(request, 'visitPerfil.html', data)










