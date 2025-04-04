import random
import time
cpu = random.randint(1,3)

print('Vamos jogar Jokempo?')
jogador = input('Insira 1 para pedra, 2 par papel e 3 para tesoura: ')

print('JO')
time.sleep(0.5)
print('KEM')
time.sleep(0.5)
print('PO')
time.sleep(0.5)

if jogador == "1":
    print('\nJogador; Pedra')
elif jogador == "2":
    print('\nJogador: Papel')
elif jogador == "3":
    print('\nJogador: Tesoura')
else:
    print('\nNúmero inválido')

if cpu == 1:
    print("Computador: Pedra")
elif cpu == 2:
    print('Computador: Papel')
elif cpu == 3:
    print('Computador: Tesoura')
else:
    print('???')


