from typing import List
from models.conta import Conta
from models.cliente import Cliente
from time import sleep


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=' * 50)
    print('BANCO'.center(50, '='))
    print('Projeto Banco'.center(50, '='))
    print('=' * 50)

    print('''
    Selecione uma opção no menu:
    1) Criar conta
    2) Efetuar saque
    3) Efetuar depósito
    4) Efetuar transferência
    5) Listar contas
    6) Sair do sistema
    ''')

    while True:
        try:
            opcao: int = int(input('Digite sua opção: '))
            break
        except:
            print('Digite um número.\n')

    match opcao:
        case 1:
            criar_conta()
        case 2:
            efetuar_saque()
        case 3:
            efetuar_deposito()
        case 4:
            efetuar_transferencia()
        case 5:
            listar_contas()
        case 6:
            print('Volte sempre!!!')
            sleep(1)
            exit(0)
        case _:
            print('Opção inválida!\n')
            sleep(1)
            menu()


def criar_conta() -> None:
    print('Informe os dados do cliente:')

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)

    print(f'''
    Conta criada com sucesso.
    Dados da conta:
    ''')
    print(conta)
    sleep(3)
    menu()


def efetuar_saque() -> None:
    pass


def efetuar_deposito() -> None:
    pass


def efetuar_transferencia() -> None:
    pass


def listar_contas() -> None:
    pass


def buscar_conta_por_numero(numero: int) -> Conta:
    pass


if __name__ == '__main__':
    main()