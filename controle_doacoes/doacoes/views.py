from typing import Any

from django.shortcuts import render, redirect
from .forms import contato, endereco, formOng, formUser, formPubliDoador, formPubliOng, formOngUp, formUserUp
from .models import Doador, Ong, Publicacao_Ong, Publicacao_Doador, Endereco, Numero_Contato

data = {}

def visitPerfilNotLog(request,pk):
    dadosOng = Ong.objects.all()
    dadosDoa = Doador.objects.all()
    for dado in dadosOng:
        if pk == dado.nome:
            perfilVisitado = Ong.objects.all().get(nome=pk)
            endVisitado = Endereco.objects.get(logradouro=perfilVisitado.id_endereco)
            telefone = Numero_Contato.objects.get(telefone=perfilVisitado.id_numero)
            postagensVisitado = Publicacao_Ong.objects.filter(id_ong=perfilVisitado).order_by('-data_publicacao')
            data['perfilVisitado'] = perfilVisitado
            data['tipoVisitado'] = 'ong'
            data['endVisitado'] = endVisitado
            data['telefone'] = telefone
            data['postagensVisitado'] = postagensVisitado
            return render(request, 'visitPerfilNotLog.html', data)

    for dado in dadosDoa:
        if pk == dado.nome:
            perfilVisitado = Doador.objects.all().get(nome=pk)
            endVisitado = Endereco.objects.get(logradouro=perfilVisitado.id_endereco)
            telefone = Numero_Contato.objects.get(telefone=perfilVisitado.id_numero)
            postagensVisitado = Publicacao_Doador.objects.filter(id_doador=perfilVisitado).order_by('-data_publicacao')
            data['perfilVisitado'] = perfilVisitado
            data['telefone'] = telefone
            data['tipoVisitado'] = 'doador'
            data['endVisitado'] = endVisitado
            data['postagensVisitado'] = postagensVisitado
            return render(request, 'visitPerfilNotLog.html', data)

def recoverPass(request):
    if request.POST:
        email = request.POST['emailRec']
        cpf = request.POST['cpfRec']
        senha = request.POST['senhaRec']
        dadoUser = Doador.objects.all()
        dadoOng = Ong.objects.all()

        for dados in dadoUser:
            if dados.email_doador == email and dados.cpf == cpf:
                dados.senha = senha
                dados.save()
                return redirect('url_login')

        for dadosOng in dadoOng:
            if dadosOng.email_ong == email and dadosOng.cnpj == cpf:
                dadosOng.senha = senha
                dadosOng.save()
                return redirect('url_login')

        data['erroRec'] = True
    return render(request, 'RecuperarSenha.html', data)

def anuncioOngs(request):
    postAnunc = Publicacao_Ong.objects.filter(categoria="EVENTO").order_by('-data_publicacao')
    data['postAnunc'] = postAnunc
    return render(request, 'anunciosOngs.html', data)

def home(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    return render(request, 'home.html', data)

def homePostOng(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postOngs = Publicacao_Ong.objects.all().order_by('-data_publicacao').exclude(id_ong=data['userLog'].pk)
    data['postOngs'] = postOngs
    data['postDoadores'] = False
    return render(request, 'home.html',data)

def homePostDoador(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html',data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postDoador = Publicacao_Doador.objects.order_by('-data_publicacao').exclude(id_doador=data['userLog'].pk)
    data['postOngs'] = False
    data['postDoadores'] = postDoador
    return render(request,'home.html',data)

def homePostEventos(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html',data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postEventos = Publicacao_Doador.objects.filter(categoria="EVENTO").order_by('-data_publicacao')
    data['postEventos'] = postEventos
    postEventosOng = Publicacao_Ong.objects.filter(categoria="EVENTO").order_by('-data_publicacao')
    data['postEventosOng'] = postEventosOng
    return render(request, 'homeEventos.html',data)

def homePostCalcados(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html',data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postCal = Publicacao_Doador.objects.filter(categoria="CALÇADO").order_by('-data_publicacao')
    postCalOng = Publicacao_Ong.objects.filter(categoria="CALÇADO").order_by('-data_publicacao')
    data['postCalOng'] = postCalOng
    data['postCal'] = postCal
    return render(request, 'homeCal.html',data)


def homePostRoupas(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html',data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postRoupas = Publicacao_Doador.objects.filter(categoria="ROUPA").order_by('-data_publicacao')
    postRoupasOng = Publicacao_Ong.objects.filter(categoria="ROUPA").order_by('-data_publicacao')
    data['postRoupasOng'] = postRoupasOng
    data['postRoupas'] = postRoupas
    return render(request, 'homeRoupas.html',data)

def homePostAlimentos(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html',data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postAlimentos = Publicacao_Doador.objects.filter(categoria="ALIMENTO").order_by('-data_publicacao')
    postAlimentosOng = Publicacao_Ong.objects.filter(categoria="ALIMENTO").order_by('-data_publicacao')
    data['postAlimentosOng'] = postAlimentosOng
    data['postAlimentos'] = postAlimentos
    return render(request, 'homeAlimentos.html',data)

def homePostMoveis(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html',data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postMoveis = Publicacao_Doador.objects.filter(categoria="MÓVEL").order_by('-data_publicacao')
    postMoveisOng = Publicacao_Ong.objects.filter(categoria="MÓVEL").order_by('-data_publicacao')
    data['postMoveisOng'] = postMoveisOng
    data['postMoveis'] = postMoveis
    return render(request, 'homeMoveis.html',data)

def homePostEletrodomesticos(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html',data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postEletro = Publicacao_Doador.objects.filter(categoria="ELETRODOMÉSTICO").order_by('-data_publicacao')
    postEletroOng = Publicacao_Ong.objects.filter(categoria="ELETRODOMÉSTICO").order_by('-data_publicacao')
    data['postEletroOng'] = postEletroOng
    data['postEletro'] = postEletro
    return render(request, 'homeEletro.html',data)

def homePostDoacao(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'home.html',data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    postDoacao = Publicacao_Doador.objects.filter(categoria="DOAÇÃO").order_by('-data_publicacao')
    data['postDoacao'] = postDoacao
    postDoacaoOng = Publicacao_Ong.objects.filter(categoria="DOAÇÃO").order_by('-data_publicacao')
    data['postDoacaoOng'] = postDoacaoOng
    return render(request, 'homeDoacao.html',data)

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
                searchOng = Ong.objects.all()
                searchDoador = Doador.objects.all()
                data['searchOng'] = searchOng
                data['searchDoador'] = searchDoador
                data['userLog'] = userLog
                data['tipoUser'] = "doador"
                return redirect('url_homePostOng')

        for dadosOng in dadoOng:
            if dadosOng.email_ong == email and dadosOng.senha == senha:
                data['acesso'] = True
                userLog = Ong.objects.all().get(email_ong=email, senha=senha)
                searchOng = Ong.objects.all()
                searchDoador = Doador.objects.all()
                data['searchOng'] = searchOng
                data['searchDoador'] = searchDoador
                data['userLog'] = userLog
                data['tipoUser'] = "ong"
                return redirect('url_homePostDoador')

        data['erroLogin'] = True
        return render(request, 'login.html', data)

    return render(request, 'login.html')


def cadastroEndeOng(request):
    form = endereco(request.POST or None, request.FILES or None) #formulario de Endereço
    formCont = contato(request.POST or None, request.FILES or None) # formulário de contato
    if form.is_valid() and formCont.is_valid():
        form.save()
        formCont.save()
        return redirect('url_cadOng')
    data['formEndOng'] = form
    data['formCont'] = formCont
    return render(request, 'cadastroEndeOng.html', data)

def cadastroOng(request):
    if request.POST and request.FILES:
        nomeOng = request.POST['nomeOng']
        cnpj = request.POST['cnpj']
        emailOng = request.POST['emailOng']
        senhaOng = request.POST['senhaOng']
        imgPerfilOng = request.FILES['imgPerfil1'] 
        endereco = Endereco.objects.latest('pk')
        telefone = Numero_Contato.objects.latest('pk')
        Ong.objects.create(nome=nomeOng,cnpj=cnpj,email_ong=emailOng,senha=senhaOng,imagem=imgPerfilOng,id_endereco=endereco,id_numero=telefone)
        return redirect('url_login')
    return render(request, 'cadastroOng.html', data)

def cadastroUser(request):
    if request.POST and request.FILES:
        nomeDoador = request.POST['nomeDoador']
        cpf = request.POST['cpf']
        emailDoador = request.POST['emailDoador']
        senhaDoador = request.POST['senhaDoador']
        imgPerfilDoador = request.FILES['imgPerfil1'] 
        endereco = Endereco.objects.latest('pk')
        telefone = Numero_Contato.objects.latest('pk')
        Doador.objects.create(nome=nomeDoador,cpf=cpf,email_doador=emailDoador,senha=senhaDoador,imagem=imgPerfilDoador,id_endereco=endereco,id_numero=telefone)
        return redirect('url_login')
    return render(request, 'cadastroUser.html', data)

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
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'perfil.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    if data['tipoUser'] == "doador":
        postagens = Publicacao_Doador.objects.filter(id_doador=data['userLog']).order_by('-data_publicacao')
        data['posts'] = postagens
        return render(request, 'perfil.html', data)
    elif data['tipoUser'] == "ong":
        postagens = Publicacao_Ong.objects.filter(id_ong=data['userLog']).order_by('-data_publicacao')
        data['posts'] = postagens
        return render(request, 'perfil.html', data)


def infos(request, pk):
    if data['tipoUser'] == "ong":
        dadosGerais = Ong.objects.get(pk = pk)
        formUpdate = formOngUp(request.POST or None,request.FILES or None,instance=dadosGerais)
        user = Ong.objects.get(pk=data['userLog'].pk)
    elif data['tipoUser'] == "doador":
        dadosGerais = Doador.objects.get(pk = pk)
        formUpdate = formUserUp(request.POST or None,request.FILES or None,instance=dadosGerais)
        user = Doador.objects.get(pk=data['userLog'].pk)

    dadosEnde = Endereco.objects.get(logradouro = user.id_endereco)
    formUpdateEnd = endereco(request.POST or None, request.FILES or None, instance=dadosEnde)

    formUpdateCont = contato(request.POST or None, request.FILES or None, instance=user.id_numero)
    if formUpdate.is_valid():
        if data['tipoUser'] == "doador":
            if request.FILES:
                nome = formUpdate.cleaned_data['nome']
                email = formUpdate.cleaned_data['email_doador']
                cpf = formUpdate.cleaned_data['cpf']
                senha = formUpdate.cleaned_data['senha']
                img = request.FILES['imgPerfil1']
                doador = Doador.objects.get(nome=data['userLog'])
                doador.nome = nome
                doador.senha = senha
                doador.cpf = cpf
                doador.email_doador = email
                doador.imagem = img
                doador.save()
                data['userLog'] = doador
            else:
                nome = formUpdate.cleaned_data['nome']
                email = formUpdate.cleaned_data['email_doador']
                cpf = formUpdate.cleaned_data['cpf']
                senha = formUpdate.cleaned_data['senha']
                doador = Doador.objects.get(nome=data['userLog'])
                doador.nome = nome
                doador.senha = senha
                doador.cpf = cpf
                doador.email_doador = email
                doador.save()
                data['userLog'] = doador

        elif data['tipoUser'] == "ong":
            if request.FILES:
                nome = formUpdate.cleaned_data['nome']
                email = formUpdate.cleaned_data['email_ong']
                cnpj = formUpdate.cleaned_data['cnpj']
                senha = formUpdate.cleaned_data['senha']
                img = request.FILES['imgPerfil1']
                ong = Ong.objects.get(nome=data['userLog'])
                ong.nome = nome
                ong.senha = senha
                ong.cnpj = cnpj
                ong.email_ong = email
                ong.imagem = img
                ong.save()
                data['userLog'] = ong
            else:
                nome = formUpdate.cleaned_data['nome']
                email = formUpdate.cleaned_data['email_ong']
                cnpj = formUpdate.cleaned_data['cnpj']
                senha = formUpdate.cleaned_data['senha']
                ong = Ong.objects.get(nome=data['userLog'])
                ong.nome = nome
                ong.senha = senha
                ong.cnpj = cnpj
                ong.email_ong = email
                ong.save()
                data['userLog'] = ong
        return redirect('url_infos',pk)
    if formUpdateEnd.is_valid():
        formUpdateEnd.save()
        return redirect('url_infos', pk)
    if formUpdateCont.is_valid():
        formUpdateCont.save()
        return redirect('url_infos', pk)
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'infos.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    data['formUpdate'] = formUpdate
    data['formUpdateEnd'] = formUpdateEnd
    data['formCont'] = formUpdateCont
    data['userUp'] = user
    return render(request, 'infos.html', data)


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
        if request.FILES:
            titulo = form.cleaned_data['titulo']
            desc = form.cleaned_data['descricao']
            catg = form.cleaned_data['categoria']
            img = request.FILES['imgPost']
            publicacao.titulo = titulo
            publicacao.descricao = desc
            publicacao.categoria = catg
            publicacao.imagem = img
            publicacao.save()
            return redirect('url_perfil')
        else:
            titulo = form.cleaned_data['titulo']
            desc = form.cleaned_data['descricao']
            catg = form.cleaned_data['categoria']
            publicacao.titulo = titulo
            publicacao.descricao = desc
            publicacao.categoria = catg
            publicacao.save()
            return redirect('url_perfil')
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'editPostOng.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    data['formEditPostOng'] = form
    data['publicacao'] = publicacao
    return render(request, 'editPostOng.html', data)

def editPostDoador(request,pk):
    publicacao = Publicacao_Doador.objects.get(pk=pk)
    form = formPubliDoador(request.POST or None,request.FILES or None, instance=publicacao)
    if form.is_valid():
        if request.FILES:
            titulo = form.cleaned_data['titulo']
            desc = form.cleaned_data['descricao']
            catg = form.cleaned_data['categoria']
            img = request.FILES['imgPost']
            publicacao.titulo = titulo
            publicacao.descricao = desc
            publicacao.categoria = catg
            publicacao.imagem = img
            publicacao.save()
            return redirect('url_perfil')
        else:
            titulo = form.cleaned_data['titulo']
            desc = form.cleaned_data['descricao']
            catg = form.cleaned_data['categoria']
            publicacao.titulo = titulo
            publicacao.descricao = desc
            publicacao.categoria = catg
            publicacao.save()
            return redirect('url_perfil')
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'editPostDoador.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    data['formEditPostDoador'] = form
    data['publicacao'] = publicacao
    return render(request, 'editPostDoador.html', data)


def newPost(request,pk):
    form = formPubliDoador(request.POST or None, request.FILES or None)
    if form.is_valid():
        if request.FILES:
            titulo = form.cleaned_data['titulo']
            desc = form.cleaned_data['descricao']
            categ = form.cleaned_data['categoria']
            img = request.FILES['imgPost']
            doador = data['userLog']
            Publicacao_Doador.objects.create(titulo=titulo,descricao=desc,categoria=categ,imagem=img,id_doador=doador)
            return redirect('url_perfil')
    # Código de Pesquisa de Usuário        
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'newPost.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    data['formPost'] = form
    return render(request, 'newPost.html', data)


def newPostOng(request,pk):
    form = formPubliOng(request.POST or None, request.FILES or None)
    if form.is_valid():
        if request.FILES:
            titulo = form.cleaned_data['titulo']
            desc = form.cleaned_data['descricao']
            categ = form.cleaned_data['categoria']
            img = request.FILES['imgPost']
            ong = data['userLog']
            Publicacao_Ong.objects.create(titulo=titulo,descricao=desc,categoria=categ,imagem=img,id_ong=ong)
            return redirect('url_perfil')
    # Código de Pesquisa de Usuário        
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'newPost.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    data['formPost'] = form
    return render(request, 'newPost.html', data)



def visitPerfil(request, pk):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'visitPerfil.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    dadosOng = Ong.objects.all()
    dadosDoa = Doador.objects.all()
    for dado in dadosOng:
        if pk == dado.nome:
            perfilVisitado = Ong.objects.all().get(nome=pk)
            endVisitado = Endereco.objects.get(logradouro = perfilVisitado.id_endereco)
            telefone = Numero_Contato.objects.get(telefone=perfilVisitado.id_numero)
            postagensVisitado = Publicacao_Ong.objects.filter(id_ong=perfilVisitado).order_by('-data_publicacao')
            data['perfilVisitado'] = perfilVisitado
            data['tipoVisitado'] = 'ong'
            data['endVisitado'] = endVisitado
            data['telefone'] = telefone
            data['postagensVisitado'] = postagensVisitado
            return render(request, 'visitPerfil.html', data)

    for dado in dadosDoa:
        if pk == dado.nome:
            perfilVisitado = Doador.objects.all().get(nome=pk)
            endVisitado = Endereco.objects.get(logradouro=perfilVisitado.id_endereco)
            telefone = Numero_Contato.objects.get(telefone=perfilVisitado.id_numero)
            postagensVisitado = Publicacao_Doador.objects.filter(id_doador=perfilVisitado).order_by('-data_publicacao')
            data['perfilVisitado'] = perfilVisitado
            data['telefone'] = telefone
            data['tipoVisitado'] = 'doador'
            data['endVisitado'] = endVisitado
            data['postagensVisitado'] = postagensVisitado
            return render(request, 'visitPerfil.html', data)


def search(request):
    if request.POST:
        nomeSearch = request.POST.get('searchName')
        if nomeSearch == "":
            return render(request, 'searchPerfil.html', data)
        else:
            compatibleUserOng = Ong.objects.filter(nome__contains=nomeSearch)
            compatibleUserDoador = Doador.objects.filter(nome__contains=nomeSearch)
            data['compatibleUserOng'] = compatibleUserOng
            data['compatibleUserDoador'] = compatibleUserDoador
            return redirect('url_search')
    return render(request, 'searchPerfil.html', data)

