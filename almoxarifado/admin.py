from django.contrib import admin
from .models import Colaborador, Ativo, Movimentacao

# Register your models here.

admin.site.register(Colaborador)
admin.site.register(Ativo)
admin.site.register(Movimentacao)