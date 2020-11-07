from django.contrib import admin
from .models import Endereco, Numero_Contato, Publicacao_Doador, Publicacao_Ong, Chat, Ong, Doador

# Register your models here.
admin.site.register(Endereco)
admin.site.register(Numero_Contato)
admin.site.register(Publicacao_Doador)
admin.site.register(Publicacao_Ong)
admin.site.register(Chat)
admin.site.register(Ong)
admin.site.register(Doador)
