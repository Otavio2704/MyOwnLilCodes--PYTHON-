import time

opcao = 0
v = None
i = None
r = None




while opcao != 4:
    opcao = int(input('\nEsta é uma calculadora de Lei de Ohm.'
              '\nO que deseja calcular?'
              '\n1- Tensão'
              '\n2- Intensidade da corrente'
              '\n3- Resistência do circuito'
              '\n4- Encerrar sessão ------>  '))
    if opcao == 1:
        i = float(input('\nInisra a corrente do circuito (Em ampére):  '))
        r = float(input('Agora insira a resistência (Em ohm): '))

        v = i*r

        print('\nCalculando...')
        time.sleep(3)

        print(f'A tensão do circuito é {v:.2f}V (voltz)')
        time.sleep(2)

    elif opcao == 2:
        v = float(input('\nInsira a tensão da corrente (em voltz): '))
        r = float(input('Agora insira a resistência (Em ohm): '))

        i= v/r

        print('\nCalculando...')
        time.sleep(3)

        print(f'A intensidade da corrente é de {i:.2f}A (ampére)')
        time.sleep(2)

    elif opcao == 3:
        v = float(input('\nInsira a tensão da corrente (em voltz): '))
        i = float(input('\nInisra a corrente do circuito (Em ampére):  '))

        r=v/i

        print('\nCalculando...')
        time.sleep(3)

        print(f'A intensidade da corrente é de {r:.2f}Ω(ohm)')
        time.sleep(2)

    elif opcao == 4:
        print('\nAté a próxima ;)')
