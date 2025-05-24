# === CLASSE DOS ELEITORES ===
class Eleitor:
    def __init__(self, cpf):
        self.cpf = cpf
        self.votou = False

# === CLASSE DOS CANDIDATOS ===
class Candidato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.votos = 0

    def receber_voto(self):
        self.votos += 1

# === CLASSE DA ELEIÇÃO ===
class Eleicao:
    def __init__(self):
        self.eleitores = {}
        self.candidatos = []
        self.votos_brancos = 0
        self.votos_nulos = 0
    
    def cadastrar_candidato(self, nome, numero):
        candidato = Candidato(nome, numero)
        self.candidatos.append(candidato)

    def encontrar_candidato(self, numero):
        for candidato in self.candidatos:
            if candidato.numero == numero:
                return candidato
        return None

    def votar(self, cpf, numero_candidato):
        eleitor = self.eleitores.get(cpf)

        if eleitor and eleitor.votou:
            print("\n❌ Este CPF já votou.")
            return

        if not eleitor:
            eleitor = Eleitor(cpf)
            self.eleitores[cpf] = eleitor

        if numero_candidato == 0:
            self.votos_brancos += 1
            print("\n✅ Voto em branco registrado.")
        else:
            candidato = self.encontrar_candidato(numero_candidato)
            if not candidato:
                self.votos_nulos += 1
                print("\n⚠️ Voto nulo registrado. Número inválido.")
            else:
                candidato.receber_voto()
                print(f"\n✅ Voto registrado para {candidato.nome}!")

        eleitor.votou = True

    def apurar_resultados(self):
        total_votos = sum(c.votos for c in self.candidatos) + self.votos_brancos + self.votos_nulos

        print("\n📊 Resultado da Eleição:")
        if total_votos == 0:
            print("Nenhum voto registrado.")
            return

        for candidato in self.candidatos:
            percentual = (candidato.votos / total_votos) * 100
            print(f"{candidato.nome} ({candidato.numero}) - {candidato.votos} votos ({percentual:.2f}%)")

        percentual_branco = (self.votos_brancos / total_votos) * 100
        percentual_nulo = (self.votos_nulos / total_votos) * 100

        print(f"Votos em branco: {self.votos_brancos} ({percentual_branco:.2f}%)")
        print(f"Votos nulos: {self.votos_nulos} ({percentual_nulo:.2f}%)")

    def exibir_vencedores(self):
        if not self.candidatos:
            print("Nenhum candidato cadastrado.")
            return

        max_votos = max(c.votos for c in self.candidatos)
        vencedores = [c for c in self.candidatos if c.votos == max_votos]

        if max_votos == 0:
            print("\n🏆 Nenhum candidato recebeu votos.")
            return

        print("\n🏆 Vencedor(es):")
        for vencedor in vencedores:
            print(f"{vencedor.nome} com {vencedor.votos} votos.")

# ===== MENU PRINCIPAL =====

eleicao = Eleicao()

# CANDIDATOS
eleicao.cadastrar_candidato("Lule", 13)
eleicao.cadastrar_candidato("Bouzonaru", 22)
eleicao.cadastrar_candidato("Gustava Limo", 51)

print("\n=== URNA ELETRÔNICA ===")

while True:
    cpf = input("\nInforme seu CPF (ou 'sair' para encerrar): ")
    if cpf.lower() == 'sair':
        break

    print("\nCandidatos:")
    for candidato in eleicao.candidatos:
        print(f"{candidato.nome} ({candidato.numero})")
    print("0 - Voto em BRANCO")

    try:
        numero = int(input("Digite o número do candidato (ou 0 para voto em branco): "))
    except ValueError:
        print("\n❌ Número inválido!")
        continue

    eleicao.votar(cpf, numero)

# Apuração dos resultados
eleicao.apurar_resultados()
eleicao.exibir_vencedores()
