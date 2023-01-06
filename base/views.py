from django.shortcuts import render
from base.forms import ContatoForm
from base.models import Contato
from base.models import ReservaForm
from base.models import Reserva



def index(request):
    return render(request, 'index.html')

def reserva(request):
    sucesso = False
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(99) 99999-9999',
        'responsavel': 'William Santos',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'reserva.html', contexto)
  
def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(71) 95555-5555',
        'responsavel': 'William Santos',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)
