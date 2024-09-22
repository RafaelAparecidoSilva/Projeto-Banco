from datetime import date
from utils.helper import str_para_date
from utils.helper import date_para_str
from utils.helper import cpf_com_mascara


class Cliente:
    contador: int = 101

    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__contador: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf_com_mascara(cpf)
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1