from datetime import date
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # Inicializando formado padrão pt-br


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    return locale.currency(valor, grouping=True, symbol=True)


def input_numero_int(texto_entrada):
    while True:
        try:
            numero: int = int(input(f'{texto_entrada}: ').strip())
            break
        except ValueError:
            print('Digite um número.\n')
    return numero


def input_numero_float(texto_entrada):
    while True:
        try:
            valor: int = int(input(f'{texto_entrada}: ').strip())
            break
        except ValueError:
            print('Digite um valor.\n')
    return valor