import time
import random

class Sim:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.energia = 100
        self.diversao = 100
        self.higiene = 100
        self.vivo = True

    def status(self):
        return {
            "Fome": self.fome,
            "Energia": self.energia,
            "Diversão": self.diversao,
            "Higiene": self.higiene,
        }

    def mostrar_status(self):
        print(f"\nStatus de {self.nome}:")
        for k, v in self.status().items():
            print(f"{k}: {v}")

    def checar_estado(self):
        for valor in self.status().values():
            if valor <= 0:
                self.vivo = False
                print(f"\n :( {self.nome} não conseguiu sobreviver. Fim de jogo.")
                break

    def comer(self):
        print(f"\n{self.nome} está comendo.")
        self.fome = min(100, self.fome + 30)
        self.energia -= 10

    def dormir(self):
        print(f"\n{self.nome} está dormindo.")
        self.energia = min(100, self.energia + 50)
        self.higiene -= 10

    def tomar_banho(self):
        print(f"\n{self.nome} está tomando banho.")
        self.higiene = min(100, self.higiene + 40)
        self.energia -= 5

    def trabalhar(self):
        print(f"\n{self.nome} está trabalhando.")
        self.energia -= 30
        self.fome -= 20
        self.diversao -= 20
        self.higiene -= 10

    def assistir_tv(self):
        print(f"\n{self.nome} está assistindo TV.")
        self.diversao = min(100, self.diversao + 25)
        self.energia -= 10
        self.fome -= 5

    def passar_tempo(self):
        self.fome -= random.randint(5, 10)
        self.energia -= random.randint(3, 8)
        self.diversao -= random.randint(5, 10)
        self.higiene -= random.randint(2, 5)
        self.checar_estado()

def simular_jogo():
    sim = Sim("Alex")
    acoes = {
        "1": sim.comer,
        "2": sim.dormir,
        "3": sim.tomar_banho,
        "4": sim.trabalhar,
        "5": sim.assistir_tv,
    }

    rodada = 0
    while sim.vivo:
        rodada += 1
        print(f"\n=== Dia {rodada} ===")
        sim.mostrar_status()

        print("\nEscolha uma ação:")
        print("1. Comer")
        print("2. Dormir")
        print("3. Tomar banho")
        print("4. Trabalhar")
        print("5. Assistir TV")
        escolha = input("Ação (1-5): ").strip()

        if escolha in acoes:
            acoes[escolha]()
        else:
            print("Escolha inválida. Nada aconteceu.")

        sim.passar_tempo()
        time.sleep(1)

    print("\n⛔ Fim da simulação.")

simular_jogo()
