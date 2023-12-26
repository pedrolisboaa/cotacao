from django.shortcuts import render
from .models import Moeda


# Create your views here.
def index(request):
    
    moedas = Moeda.objects.all()
    
    context = {
        'moedas': moedas,
    }
    
    return render(request, 'index.html', context)