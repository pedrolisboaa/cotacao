from django.shortcuts import render
from .models import Moeda
from util.cotacao import cotacao_moeda, valor_conversao
from util.data import data_formatada


# Create your views here.
def index(request):
    moedas = Moeda.objects.all()
    real = Moeda.objects.get(pk='11')
    dolar = Moeda.objects.get(pk='1')
    valor_atualizado = None


    valor_dolar = cotacao_moeda(dolar.sigla)
    context = {
            'moedas': moedas,
            'data': data_formatada(),
            'real': real,
            'dolar': dolar,
            'valor_atualizado': valor_atualizado,
            'valor_dolar': valor_dolar,
        }


    if request.method == 'POST':
        moeda_sigla = request.POST.get('moeda')
        moeda_cotacao = request.POST.get('moeda_cotacao')

        
        valor_atualizado = valor_conversao(cotacao_moeda(moeda_sigla), moeda_cotacao)
        
        print(valor_atualizado)
    

        context = {
            'moedas': moedas,
            'data': data_formatada(),
            'real': real,
            'dolar': dolar,
            'valor_atualizado': valor_atualizado,
            'valor_dolar': valor_dolar,
        }
         
    return render(request, 'index.html', context)