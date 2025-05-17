import time

def calcular_tensao():
    i = float(input('\nInsira a corrente do circuito (em ampère): '))
    r = float(input('Agora insira a resistência (em ohm): '))
    v = i * r
    print('\nCalculando...')
    time.sleep(3)
    print(f'A tensão do circuito é {v:.2f}V (volt)')
    time.sleep(2)

def calcular_corrente():
    v = float(input('\nInsira a tensão da corrente (em volt): '))
    r = float(input('Agora insira a resistência (em ohm): '))
    i = v / r
    print('\nCalculando...')
    time.sleep(3)
    print(f'A intensidade da corrente é de {i:.2f}A (ampère)')
    time.sleep(2)

def calcular_resistencia():
    v = float(input('\nInsira a tensão da corrente (em volt): '))
    i = float(input('Insira a corrente do circuito (em ampère): '))
    r = v / i
    print('\nCalculando...')
    time.sleep(3)
    print(f'A resistência do circuito é de {r:.2f}Ω (ohm)')
    time.sleep(2)

def exibir_menu():
    print('\nEsta é uma calculadora de Lei de Ohm.')
    print('O que deseja calcular?')
    print('1 - Tensão')
    print('2 - Intensidade da corrente')
    print('3 - Resistência do circuito')
    print('4 - Encerrar sessão')

def main():
    while True:
        exibir_menu()
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                calcular_tensao()
            elif opcao == 2:
                calcular_corrente()
            elif opcao == 3:
                calcular_resistencia()
            elif opcao == 4:
                print('\nAté a próxima ;)')
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Digite um número.')

if __name__ == "__main__":
    main()
