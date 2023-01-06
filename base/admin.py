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
