from django.db import models
import getpass

# Create your models here.

class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=100, verbose_name="Endereço")
    numero = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


    def __str__(self):
        return self.logradouro

    class Meta:
        verbose_name_plural = "Endereços"



class Ong(models.Model):
    id_ong = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=100, verbose_name="CNPJ")
    nome = models.CharField(max_length=100, verbose_name="Nome da Ong")
    email_ong = models.EmailField(max_length=100, verbose_name="E-mail da Ong", null=True, blank=True)
    senha = models.CharField(max_length=100)
    imagem = models.FileField(upload_to="perfil_ong/%Y/%m/%d/", null=True, blank=True)
    id_endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Ongs"


class Doador(models.Model):
    id_doador = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    nome = models.CharField(max_length=100, verbose_name="Nome do Doador", null=True)
    email_doador = models.EmailField(max_length=100, verbose_name="E-mail do Doador", null=True, blank=True)
    senha = models.CharField(max_length=100, null=True, blank=True)
    imagem = models.FileField(upload_to="perfil_doador/%Y/%m/%d/", null=True, blank=True)
    id_endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Doadores"


class Numero_Contato(models.Model):
    id_numero = models.AutoField(primary_key=True)
    telefone = models.CharField(max_length=20)
    id_doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    id_ong = models.ForeignKey(Ong, on_delete=models.CASCADE)

    def __str__(self):
        return self.telefone


class Publicacao_Doador(models.Model):
    id_publicacao_doador = models.AutoField(primary_key=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    imagem = models.FileField(upload_to="Publicacao_doador/%Y/%m/%d/", null=True, blank=True)
    id_doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    categoria_choices = [
        ("ROUPA", "Roupa"),
        ("CALÇADO", "Calçado"),
        ("ALIMENTO", "Alimento"),
        ("MÓVEL", "Móvel"),
        ("ELETRODOMÉSTICO", "Eletrodoméstico"),
        ("EVENTO", "Evento"),
        ("DOAÇÃO", "Doação")
    ]
    categoria = models.CharField(max_length=20, choices=categoria_choices, default="DOAÇÃO")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicações dos Doadores"


class Publicacao_Ong(models.Model):
    id_publicacao_Ong = models.AutoField(primary_key=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    imagem = models.FileField(upload_to="Publicacao_ong/%Y/%m/%d/", null=True, blank=True)
    id_ong = models.ForeignKey(Ong, on_delete=models.CASCADE)
    categoria_choices = [
        ("ROUPA", "Roupa"),
        ("CALÇADO", "Calçado"),
        ("ALIMENTO", "Alimento"),
        ("MÓVEL", "Móvel"),
        ("ELETRODOMÉSTICO", "Eletrodoméstico"),
        ("EVENTO", "Evento"),
        ("DOAÇÃO", "Doação")
    ]
    categoria = models.CharField(max_length=20, choices=categoria_choices, default="DOAÇÃO")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicações das Ongs"