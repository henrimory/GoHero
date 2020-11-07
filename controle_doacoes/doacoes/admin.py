from django.contrib import admin
from .models import Endereco, Ong, Doador, Numero_Contato, Publicacao_Doador, Publicacao_Ong

# Register your models here.
admin.site.register(Endereco)
admin.site.register(Ong)
admin.site.register(Doador)
admin.site.register(Numero_Contato)
admin.site.register(Publicacao_Doador)
admin.site.register(Publicacao_Ong)
