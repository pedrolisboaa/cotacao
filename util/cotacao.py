import requests

def cotacao_moeda(codigo_moeda):
    URL = f'http://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL'
    request = requests.get(URL)
    dicionario_moeda = request.json()
    valor_moeda = dicionario_moeda[f'{codigo_moeda}BRL']['bid']
    #return dicionario_moeda
    return float(valor_moeda)


def valor_conversao(valor1, valor2):
    if valor2 == None:
        valor2 = 1
    
    resultado = float(valor1) * float(valor2.replace(",", "."))
    resultado_arredondado = round(resultado, 2)
    return resultado_arredondado