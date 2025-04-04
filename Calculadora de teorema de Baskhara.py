import math
import time

result1 = 0
result2 = 0
va= float(input('insira o valor de a: '))
vb= float(input('Agora insira o valor de b: '))
vc= float(input('E por último o valor de c: '))

result1 = -vb+math.sqrt(4*va*vc)/2*va
result2 = -vb-math.sqrt(4*va*vc)/2*va

print('\nCalculando')
time.sleep(3)

print(f'\n o valor da raíz 1 é igual a {result1:.2f} e da raíz 2 é igual a {result2:.2f}')

