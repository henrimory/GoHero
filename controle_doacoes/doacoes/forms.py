from django.forms import ModelForm
from doacoes.models import Numero_Contato, Endereco, Ong, Doador, Publicacao_Doador, Publicacao_Ong


class contato(ModelForm):
     class Meta:
       model = Numero_Contato
       fields = ['telefone']


class endereco(ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro','numero','bairro','cidade']


class formOng(ModelForm):
    class Meta:
        model = Ong
        fields = ['nome','cnpj','email_ong','senha','imagem','id_endereco','id_numero']


class formUser(ModelForm):
    class Meta:
        model = Doador
        fields = ['nome','cpf','email_doador','senha','imagem','id_endereco','id_numero']


class formOngUp(ModelForm):
    class Meta:
        model = Ong
        fields = ['nome','cnpj','email_ong','senha']


class formUserUp(ModelForm):
    class Meta:
        model = Doador
        fields = ['nome','cpf','email_doador','senha']

class formPubliDoador(ModelForm):
    class Meta:
        model = Publicacao_Doador
        fields = ['titulo', 'descricao','categoria']

class formPubliOng(ModelForm):
    class Meta:
        model = Publicacao_Ong
        fields = ['titulo', 'descricao','categoria']
