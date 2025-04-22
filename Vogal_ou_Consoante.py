palavra = input('Digite uma letra: ').strip().upper()[0] 
if palavra in 'AEIOU': 
  print('Vogal') 
else:
  print('Consoante')
