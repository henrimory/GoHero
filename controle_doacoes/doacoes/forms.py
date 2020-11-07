from django.forms import ModelForm
from doacoes.models import Numero_Contato, Endereco, Ong, Doador


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
        fields = ['nome','email_ong','senha','imagem','id_endereco','Numero_Contato']


class formUser(ModelForm):
    class Meta:
        model = Doador
        fields = ['nome','email_doador','senha','imagem','id_endereco','id_endereco']
