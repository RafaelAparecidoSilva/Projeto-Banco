from typing import List
from models.conta import Conta
from models.cliente import Cliente
from time import sleep
from utils.helper import input_numero_int, input_numero_float


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

    opcao: int = input_numero_int('Digite sua opção')

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
    if len(contas) > 0:
        numero: int = input_numero_int('Informe o número da sua conta: ')

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = input_numero_float('Informe o valor do saque: ')
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')

    else:
        print('Não existem contas cadastradas.')
        sleep(2)
        menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = input_numero_int('Informe o número da sua conta: ')
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = input_numero_float('Informe o valor do depósito: ')
            conta.depositar(valor)
        else:
            print(f'Não foi encontrado a conta com o número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = input_numero_int('Informe o número da sua conta: ')
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = input_numero_int('Informe o número da conta destino: ')
            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = input_numero_float('Informe o valor da transferência: ')
                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A conta destino com número {numero_destino} não foi encontrado.')
        else:
            print(f'A sua conta, com número {numero_origem}, não foi encontrada.')

    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('-' * 30)
            sleep(1)

    else:
        print('Não existem contas cadastradas.')
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
