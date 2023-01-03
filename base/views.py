from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html')

    
def contato(request):
    return render(request, 'contato.html')
