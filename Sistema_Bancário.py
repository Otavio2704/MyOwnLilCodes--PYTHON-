import time

# Senha inicial para acessar o sistema bancário
SENHA_CORRETA = "python123"

# Função que inicia o sistema bancário
def sistema_bancario():
    opcao = 0
    dinheiro = 0
    extrato = []

    while opcao != 4:
        opcao = int(input('\nO que deseja fazer?'
                          '\n1 - Fazer depósito'
                          '\n2 - Sacar dinheiro'
                          '\n3 - Ver extrato'
                          '\n4 - Encerrar operação -----> '))

        if opcao == 1:
            ad = float(input('\nInsira o valor do depósito: '))
            if ad > 0:
                dinheiro += ad
                extrato.append(f'Depósito: +R$ {ad:.2f}')
                print('Depósito realizado com sucesso ;)')
            else:
                print('Valor inválido! O depósito deve ser positivo.')

        elif opcao == 2:
            ret = float(input('\nValor a sacar: '))
            if ret > dinheiro:
                print('Saldo insuficiente para realizar o saque.')
            elif ret <= 0:
                print('Valor inválido! O saque deve ser positivo.')
            else:
                dinheiro -= ret
                extrato.append(f'Saque: -R$ {ret:.2f}')
                print('Saque realizado com sucesso!')

        elif opcao == 3:
            print('\n--- Extrato ---')
            if not extrato:
                print('Nenhuma movimentação registrada.')
            else:
                for movimento in extrato:
                    print(movimento)
            print(f'\nSaldo atual: R$ {dinheiro:.2f}')

        elif opcao == 4:
            print('\nTenha um ótimo dia :)')

        else:
            print('\nOpção inválida, selecione as opções presentes na tela')

# Função para autenticação inicial
def autenticar():
    senha_inicial = input("Insira a senha para iniciar o sistema bancário: ")
    if senha_inicial == SENHA_CORRETA:
        sistema_bancario()
    else:
        print("Senha incorreta. Acesso negado.")

# Chama a função de autenticação antes de iniciar o sistema bancário
autenticar()
