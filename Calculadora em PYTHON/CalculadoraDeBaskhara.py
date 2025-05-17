import math
import time

def obter_valores():
    """Obtém os valores de a, b e c do usuário."""
    va = float(input('Insira o valor de a: '))
    vb = float(input('Agora insira o valor de b: '))
    vc = float(input('E por último o valor de c: '))
    return va, vb, vc

def calcular_raizes(a, b, c):
    """Calcula as raízes usando o teorema de Bhaskara."""
    delta = b**2 - 4*a*c  # Calculando o discriminante
    if delta < 0:
        return None, None  # Retorna None se não houver raízes reais
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    return raiz1, raiz2

def exibir_resultado(raiz1, raiz2):
    """Exibe o resultado das raízes calculadas."""
    print('\nCalculando')
    time.sleep(3)
    if raiz1 is None or raiz2 is None:
        print("Não há raízes reais.")
    else:
        print(f'\nO valor da raiz 1 é igual a {raiz1:.2f} e da raiz 2 é igual a {raiz2:.2f}')

def main():
    """Função principal para rodar o programa."""
    a, b, c = obter_valores()
    raiz1, raiz2 = calcular_raizes(a, b, c)
    exibir_resultado(raiz1, raiz2)

# Executa o programa
main()
