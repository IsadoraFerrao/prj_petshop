from django.contrib import admin
from .models import *

""" admin.site.register(Responsavel)
admin.site.register(CadastroPet)
admin.site.register(ReservaServico)

 """
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
   list_display = ['nome_pet', 'telefone', 'dia_reserva', 'observacoes', 'data']
   search_fields = ['nome_pet', 'dia_reserva']
   list_filter = ['dia_reserva']