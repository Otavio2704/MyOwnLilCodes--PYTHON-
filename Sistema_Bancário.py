import time

opcao = 0
dinheiro = 0
extrato = []
saques_realizados = 0  # Contador de saques no dia
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500.00

while opcao != 4:
    opcao = int(input('\nO que deseja fazer?'
                      '\n1 - Fazer depósito'
                      '\n2 - Sacar dinheiro'
                      '\n3 - Ver extrato'
                      '\n4 - Encerrar operação -----> '))

    if opcao == 1:
        senha = input('\nInsira sua senha: ')
        print('Processando...')
        time.sleep(2)
        if senha == "python123":
            ad = float(input('\nInsira o valor do depósito: '))
            if ad > 0:
                dinheiro += ad
                extrato.append(f'Depósito: +R$ {ad:.2f}')
                print('Depósito realizado com sucesso ;)')
            else:
                print('Valor inválido! O depósito deve ser positivo.')
        else:
            print('\nSenha incorreta :(')

    elif opcao == 2:
        senha = input('\nInsira sua senha: ')
        print('Processando...')
        time.sleep(2)
        if senha == "python123":
            if saques_realizados >= LIMITE_SAQUES:
                print('Limite diário de saques atingido!')
            else:
                ret = float(input('\nValor a sacar: '))
                if ret > LIMITE_SAQUE_VALOR:
                    print(f'O valor máximo por saque é de R$ {LIMITE_SAQUE_VALOR:.2f}')
                elif ret > dinheiro:
                    print('Saldo insuficiente para realizar o saque.')
                elif ret <= 0:
                    print('Valor inválido! O saque deve ser positivo.')
                else:
                    dinheiro -= ret
                    extrato.append(f'Saque: -R$ {ret:.2f}')
                    saques_realizados += 1
                    print('Saque realizado com sucesso!')
        else:
            print('Senha incorreta :(')

    elif opcao == 3:
        senha = input('\nInsira sua senha: ')
        print('Processando...')
        time.sleep(2)
        if senha == "python123":
            print('\n--- Extrato ---')
            if not extrato:
                print('Nenhuma movimentação registrada.')
            else:
                for movimento in extrato:
                    print(movimento)
            print(f'\nSaldo atual: R$ {dinheiro:.2f}')
        else:
            print('Senha incorreta :(')

    elif opcao == 4:
        print('\nTenha um ótimo dia :)')

    else:
        print('\nOpção inválida, selecione as opções presentes na tela')
