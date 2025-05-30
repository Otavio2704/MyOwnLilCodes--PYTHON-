#Função que codifica o texto oferecido pelo usuário
def codificar_cifra_cesar(texto, deslocamento):
    resultado = ""

    for char in texto:
        if char.isupper():
            codigo = ord(char) - ord('A')
            codigo = (codigo + deslocamento) % 26
            resultado += chr(codigo + ord('A'))
        elif char.islower():
            codigo = ord(char) - ord('a')
            codigo = (codigo + deslocamento) % 26
            resultado += chr(codigo + ord('a'))
        else:
            resultado += char

    return resultado

#Decodifica texto oferecido pelo usuário
def decodificar_cifra_cesar(texto, deslocamento):
    return codificar_cifra_cesar(texto, -deslocamento)

#Menu principal
def main():
    print("Cifra de César - Codificador/Decodificador\n")

    while True:
        texto = input("Digite o texto [DIGITE SEM ACENTO] ou '0' para encerrar): ")
        if texto.lower() == '0':
            print("Encerrando o programa. Até mais!")
            break

        while True:
            try:
                deslocamento = int(input("Digite o deslocamento (número inteiro): "))
                break
            except ValueError:
                print("Por favor, digite um número válido.")

        escolha = ""
        while escolha not in ['1', '2']:
            print("\nEscolha uma opção:")
            print("1 - Codificar")
            print("2 - Decodificar")
            escolha = input("Opção: ")

        if escolha == '1':
            resultado = codificar_cifra_cesar(texto, deslocamento)
            print("\nTexto codificado:")
        else:
            resultado = decodificar_cifra_cesar(texto, deslocamento)
            print("\nTexto decodificado:")

        print(resultado)
        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()
