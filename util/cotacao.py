import requests

def cotacao_moeda(codigo_moeda):
    URL = f'http://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL'
    request = requests.get(URL)
    dicionario_moeda = request.json()
    #valor_moeda = dicionario_moeda['USDBRL']['bid']
    valor_moeda = dicionario_moeda
    return dicionario_moeda
    
    #return float(valor_moeda)



#print(cotacao_moeda('KWD'))
print(cotacao_moeda('EUR'))
print(cotacao_moeda('USD'))