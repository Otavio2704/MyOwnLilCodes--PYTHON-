# Classe que representa um Filme, com nome, horários e sessões
class Filme:
    def __init__(self, nome, horarios):
        self.nome = nome
        self.horarios = horarios
        self.sessoes = {horario: Sessao(horario) for horario in horarios}

    # Função que exibe os horários disponíveis do filme
    def exibir_horarios(self):
        print(f"\nHorários para {self.nome}:")
        for horario in self.horarios:
            print(f"- {horario}")

# Classe que representa uma Sessão de cinema
class Sessao:
    def __init__(self, horario, total_cadeiras=10):
        self.horario = horario
        self.total_cadeiras = total_cadeiras
        self.cadeiras_ocupadas = set()

    # Função que mostra o status de todas as cadeiras
    def mostrar_cadeiras_disponiveis(self):
        print(f"\nCadeiras disponíveis para a sessão das {self.horario}:")
        for i in range(1, self.total_cadeiras + 1):
            status = "Ocupada" if i in self.cadeiras_ocupadas else "Livre"
            print(f"Cadeira {i}: {status}")

    # Função que tenta reservar uma cadeira
    def reservar_cadeira(self, numero):
        if numero in self.cadeiras_ocupadas:
            print(f"Cadeira {numero} já está ocupada. Por favor, escolha outra.")
            return False
        elif numero < 1 or numero > self.total_cadeiras:
            print(f"Número de cadeira inválido. Escolha entre 1 e {self.total_cadeiras}.")
            return False
        else:
            self.cadeiras_ocupadas.add(numero)
            print(f"Cadeira {numero} reservada com sucesso!")
            return True

    # Função que verifica se todas as cadeiras estão ocupadas
    def todas_ocupadas(self):
        return len(self.cadeiras_ocupadas) >= self.total_cadeiras

#Classe de filmes no cinema
class Cinema:
    def __init__(self):
        self.filmes = []

    # Função para adicionar um filme ao cinema
    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    # Função que lista todos os filmes disponíveis
    def listar_filmes(self):
        print("Bem-vindo ao Cine-Tavin"
        "\nesses são os Filmes em cartaz hoje:")
        for idx, filme in enumerate(self.filmes, start=1):
            print(f"{idx}. {filme.nome}")

    # Função que retorna um filme com base na escolha do usuário
    def escolher_filme(self, indice):
        if 0 < indice <= len(self.filmes):
            return self.filmes[indice - 1]
        else:
            print("Filme inválido.")
            return None

# --------------------
# Menu principal

# Criando o cinema
cinema = Cinema()

# Criando filmes e adicionando ao cinema
filme1 = Filme("Vingadores: Ultimato", ["14:00", "18:00"])
filme2 = Filme("Toy Story 4", ["12:00", "16:00", "20:00"])

cinema.adicionar_filme(filme1)
cinema.adicionar_filme(filme2)

# Loop principal do sistema
while True:
    cinema.listar_filmes()
    escolha_filme = int(input("\nEscolha um filme (número) ou 0 para sair: "))
    
    # Condição de saída
    if escolha_filme == 0:
        break

    filme_escolhido = cinema.escolher_filme(escolha_filme)
    
    # Se o filme for válido
    if filme_escolhido:
        while True:
            filme_escolhido.exibir_horarios()
            horario = input("Escolha um horário (ex: 14:00) ou '0' para escolher outro filme: ")

            # Opção de voltar para escolher outro filme
            if horario.lower() == "0":
                break

            # Se o horário escolhido for válido
            if horario in filme_escolhido.horarios:
                sessao = filme_escolhido.sessoes[horario]

                # Verifica se todas as cadeiras estão ocupadas
                if sessao.todas_ocupadas():
                    print("\nTodas as cadeiras dessa sessão estão ocupadas. Por favor, escolha outro horário.")
                    continue

                # Loop para reservar cadeiras
                while True:
                    sessao.mostrar_cadeiras_disponiveis()
                    try:
                        quantidade = int(input("Quantas cadeiras deseja reservar? "))
                        if quantidade <= 0 or quantidade > (sessao.total_cadeiras - len(sessao.cadeiras_ocupadas)):
                            print("Quantidade inválida ou maior que o número de cadeiras disponíveis.")
                            continue
                    except ValueError:
                        print("Por favor, insira um número válido.")
                        continue

                    #Reserva de cadeiras
                    reservadas = 0
                    while reservadas < quantidade:
                        try:
                            cadeira = int(input(f"\nEscolha o número da cadeira ({reservadas + 1}/{quantidade}): "))
                            sucesso = sessao.reservar_cadeira(cadeira)
                            if sucesso:
                                reservadas += 1
                            else:
                                print("Tente escolher outra cadeira.")  # Se cadeira ocupada, tenta novamente
                        except ValueError:
                            print("Por favor, insira um número válido.")

                    print("Reserva finalizada com sucesso!\n")
                    break  # Sai da escolha de cadeiras, volta para escolher outro filme
                break  # Sai da escolha de horário, volta para escolher outro filme
            else:
                print("Horário inválido.")
