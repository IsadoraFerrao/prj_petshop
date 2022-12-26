from django.db import models

# Create your models here.

class Reserva(models.Models):
    tipos_list = (
        ("gato", "Gato"),
        ("cachorro", "Cachorro")
    )
    tipo = models.CharField(max_length=30, verbose_name="Tipo", choices=tipos_list)
    nome = models.CharField(max_length=50, verbose_name="Nome do Pet")
    dia_dia_reserva = models.DateField(verbose_name="Dia da Reserva")
    telefone = models.CharField(max_length=14, verbose_name="Telefone")
    email = models.EmailField(verbose_name="Email")
    observacoes = models.TextField(verbose_name="Observações")



