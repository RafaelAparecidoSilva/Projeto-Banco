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