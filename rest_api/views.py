from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from reserva.models import Reserva

# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})

    return Response({'hello': 'World API'})


@api_view()
def reserva_de_banho(request):
    consulta = Reserva.objects.all()
    dados = []
    for reserva in consulta:
        dado = {
            'nome': reserva.nome,
            'email': reserva.email,
            'nome_do_pet': reserva.nome_pet,
            'data': reserva.data,
            'turno': reserva.turno,
            'tamanho': reserva.tamanho,
            'observacao': reserva.observacao,
        }
        dados.append(dado)
        return Response(dados)