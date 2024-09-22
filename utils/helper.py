from datetime import date
from datetime import datetime


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def cpf_com_mascara(cpf: str) -> str:
    cpf_sem_ponto = cpf.replace('.', '').replace(',', '').replace('-', '')
    cpf_formatado = ""
    for numero, texto in enumerate(cpf_sem_ponto):
        if numero == 3 or numero == 6:
            cpf_formatado += "." + texto
        elif numero == 9:
            cpf_formatado += "-" + texto
        else:
            cpf_formatado += texto
    return cpf_formatado

