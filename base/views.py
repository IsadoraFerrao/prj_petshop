from django.shortcuts import render
from base.forms import ContatoForm

    
def index(request):
    return render(request, 'index.html')

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
