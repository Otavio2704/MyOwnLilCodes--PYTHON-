#Analisa se a palavra é palíndromo ou não
def verificar_palindromo(palavra):
    palavra = palavra.upper().strip()
    palavra_invertida = palavra[::-1]
    
    if palavra == palavra_invertida:
        return 'Esta palavra é um palíndromo'
    else:
        return 'Esta palavra não é um palíndromo'

#Adicionar palavra
entrada = input('Insira uma palavra: ')
resultado = verificar_palindromo(entrada)
print(resultado)
