import random
import time

#Jo-Ken-Po...
def exibir_contagem():
    print('JO')
    time.sleep(0.5)
    print('KEM')
    time.sleep(0.5)
    print('PO')
    time.sleep(0.5)

#Escolher entre pedra,papel ou tesoura
def obter_escolha_jogador():
    escolha = input('Insira 1 para pedra, 2 para papel e 3 para tesoura: ')
    if escolha in ["1", "2", "3"]:
        return int(escolha)
    else:
        print('\nNúmero inválido')
        return None
#Para exibir o resultado
def mostrar_escolha(nome, escolha):
    opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
    print(f'\n{nome}: {opcoes.get(escolha, "Escolha inválida")}')

def jogar_jokempo():
    print('Vamos jogar Jokempo?')
    jogador = obter_escolha_jogador()
    if jogador is None:
        return

    cpu = random.randint(1, 3)

#Resultados
    exibir_contagem()
    mostrar_escolha('Jogador', jogador)
    mostrar_escolha('Computador', cpu)

#Executa o jogo
jogar_jokempo()
