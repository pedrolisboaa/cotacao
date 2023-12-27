from datetime import date, datetime
import calendar
import locale

def data_formatada():
    # Definindo localização 
    locale.setlocale(locale.LC_TIME, 'pt_BR')

    data_atual = date.today()
    dia = data_atual.day
    mes = calendar.month_name[data_atual.month]
    ano = data_atual.year
    hora = datetime.now().hour
    minuto = datetime.now().minute
    
    return f'{dia} de {mes} de {ano} ás {hora}:{minuto}'