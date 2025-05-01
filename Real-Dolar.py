opcao = 0

while opcao != 3:
        opcao = int(input('\nQual conversão deseja fazer?:'
                            '\n1 - Real para Dólar'
                            '\n2 - Dólar para Real'
                            '\n3 - Sair -----> '))
        if opcao == 1:
                real = float(input('\ninsira o valor em Reais: '))
                dolar = real/5.68
                print(f'O valor em Dólar é: {dolar:.2f}')
        elif opcao == 2:
                dolar = float(input('\ninsira o valor em Dólar: '))
                real = dolar*5.68
                print(f'O valor em Reais é: {real:.2f}')
        elif opcao == 3:
                print('\nTenha um ótimo dia :)')
        else:
                print('opção inválida')