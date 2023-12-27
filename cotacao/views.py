from django.shortcuts import render
from .models import Moeda
from util.cotacao import cotacao_moeda, valor_conversao
from util.data import data_formatada


# Create your views here.
def index(request):
    moedas = Moeda.objects.all()
    real = Moeda.objects.get(pk='11')
    valor_atualizado = None

    context = {
        'moedas': moedas,
        'data': data_formatada(),
        'real': real,
        'valor_atualizado': valor_atualizado,
    }
    
    if request.method == 'POST':
        moeda_sigla = request.POST.get('moeda')
        moeda_cotacao = request.POST.get('moeda_cotacao')

        
        valor_atualizado = valor_conversao(cotacao_moeda(moeda_sigla), moeda_cotacao)
        print(valor_atualizado)
         
    return render(request, 'index.html', context)