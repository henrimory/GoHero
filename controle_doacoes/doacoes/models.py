from django.db import models

# Create your models here.

class Numero_Contato(models.Model):
    id_numero = models.AutoField(primary_key=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.telefone


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.logradouro

    class Meta:
        verbose_name_plural = "Endereços"


class Ong(models.Model):
    id_ong = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, verbose_name="Nome da ong")
    email_ong = models.EmailField(max_length=100, verbose_name="E-mail da ong", null=True, blank=True)
    senha = models.CharField(max_length=100, null=True, blank=True)
    imagem = models.FileField(upload_to="perfil_ong/%Y/%m/%d/", null=True, blank=True)
    id_endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    Numero_Contato = models.ManyToManyField(Numero_Contato)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Ongs"


class Doador(models.Model):
    id_doador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, verbose_name="Nome do doador")
    email_doador = models.EmailField(max_length=100, verbose_name="E-mail do doador", null=True, blank=True)
    senha = models.CharField(max_length=100, null=True, blank=True)
    imagem = models.FileField(upload_to="perfil_doador/%Y/%m/%d/", null=True, blank=True)
    id_endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    Numero_Contato = models.ManyToManyField(Numero_Contato)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Doadores"

class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    mensagem = models.CharField(max_length=500, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)

    def __str__(self):
        return self.mensagem


class Publicacao_Doador(models.Model):
    id_publicacao_doador = models.AutoField(primary_key=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100, verbose_name="Título", null=True, blank=True)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    imagem = models.FileField(upload_to="Publicacao_doador/%Y/%m/%d/", null=True, blank=True)
    id_doador = models.ForeignKey(Doador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicações_Doadores"


class Publicacao_Ong(models.Model):
    id_publicacao_Ong = models.AutoField(primary_key=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100, verbose_name="Título", null=True, blank=True)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    imagem = models.FileField(upload_to="Publicacao_ong/%Y/%m/%d/", null=True, blank=True)
    id_ong = models.ForeignKey(Ong, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicações_Ongs"
