from django.db import models
from django.conf import settings


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(verbose_name="Data Envio", auto_now_add=True)
    def __str__(self):
        return f'{self.nome} - {self.email}'
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-data']

