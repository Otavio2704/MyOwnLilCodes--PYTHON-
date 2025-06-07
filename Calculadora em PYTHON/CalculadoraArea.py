from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(Forma):
    def _init_(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Retangulo(Forma):
    def _init_(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

class Triangulo(Forma):
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Esfera(Forma):
    def _init_(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 4 * math.pi * self.raio ** 2

class Trapezio(Forma):
    def _init_(self, base_maior, base_menor, altura):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def calcular_area(self):
        return ((self.base_maior + self.base_menor) * self.altura) / 2

class Losango(Forma):
    def _init_(self, diagonal_maior, diagonal_menor):
        self.diagonal_maior = diagonal_maior
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        return (self.diagonal_maior * self.diagonal_menor) / 2

def solicitar_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Tente novamente.")

def menu():
    print("\nQual área você deseja calcular?")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Triângulo")
    print("4 - Esfera")
    print("5 - Trapézio")
    print("6 - Losango")
    print("7 - Encerrar operação")

def main():
    opcao = 0
    while opcao != 7:
        menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue

        if opcao == 1:
            lado = solicitar_float("\nInsira o lado do quadrado: ")
            forma = Quadrado(lado)

        elif opcao == 2:
            altura = solicitar_float("\nInsira a altura do retângulo: ")
            largura = solicitar_float("Agora, insira a largura do retângulo: ")
            forma = Retangulo(altura, largura)

        elif opcao == 3:
            base = solicitar_float("\nInsira o tamanho da base: ")
            altura = solicitar_float("Agora, insira a altura do triângulo: ")
            forma = Triangulo(base, altura)

        elif opcao == 4:
            raio = solicitar_float("\nInsira o raio da esfera: ")
            forma = Esfera(raio)

        elif opcao == 5:
            base_maior = solicitar_float("\nInsira a base maior do trapézio: ")
            base_menor = solicitar_float("Agora, a base menor: ")
            altura = solicitar_float("Agora, a altura: ")
            forma = Trapezio(base_maior, base_menor, altura)

        elif opcao == 6:
            diagonal_maior = solicitar_float("\nInsira a diagonal maior do losango: ")
            diagonal_menor = solicitar_float("Agora, a diagonal menor: ")
            forma = Losango(diagonal_maior, diagonal_menor)

        elif opcao == 7:
            print("\nAté a próxima :)")
            break

        else:
            print("\nOpção inválida.")
            continue

        area = forma.calcular_area()
        print(f"\nA área total é: {area:.2f} cm²")

if _name_ == "_main_":
    main()
