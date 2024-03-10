from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulente

def ver_consulente(request, id):
    # Busca um consulente pelo ID ou retorna uma página 404 se não encontrado
    consulentes = get_object_or_404(Consulente, pk=id)
    
    # Renderiza um template, passando o consulente encontrado como contexto
    return render(request, 'home.html', {'consulentes': consulentes})

def home(request):
    pesquisa_query = request.GET.get('pesquisa', '')
    if pesquisa_query:
        consulentes = Consulente.objects.filter(nome__icontains=pesquisa_query)
    else:
        consulentes = Consulente.objects.all()
    return render(request, 'home.html', {'consulentes': consulentes})

def apagar_consulente(request, id):
    consulente = Consulente.objects.get(id=id)
    consulente.delete()
    return redirect('home')