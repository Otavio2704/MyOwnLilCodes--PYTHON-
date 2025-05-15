from datetime import datetime

# ========================= CLASSES DE TRANSACAO =========================

class Transacao:
    def registrar(self, conta):
        raise NotImplementedError()

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta._saldo += self.valor
        conta.historico.adicionar_transacao(f"[{datetime.now()}] Depósito: +R$ {self.valor:.2f}")
        print("Depósito realizado com sucesso!")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor <= 0:
            print("Valor inválido! O saque deve ser positivo.")
        elif self.valor > conta._saldo:
            print("Saldo insuficiente.")
        else:
            conta._saldo -= self.valor
            conta.historico.adicionar_transacao(f"[{datetime.now()}] Saque: -R$ {self.valor:.2f}")
            print("Saque realizado com sucesso!")

# ========================= CLASSES DE HISTÓRICO =========================

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao):
        self.transacoes.append(descricao)

# ========================= CLASSES DE CONTA =========================

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        transacao = Saque(valor)
        transacao.registrar(self)

    def depositar(self, valor):
        transacao = Deposito(valor)
        transacao.registrar(self)

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

# ========================= CLASSES DE CLIENTE =========================

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco, senha):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.senha = senha

# ========================= FUNÇÕES DO SISTEMA =========================

clientes = []
contador_conta = 1

def criar_usuario():
    print("\n--- Cadastro de Usuário ---")
    cpf = input("Informe o CPF (somente números): ").strip()

    if any(cliente.cpf == cpf for cliente in clientes):
        print("CPF já cadastrado! Usuário não pode ser duplicado.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço (logradouro/bairro/Cidade/sigla estado): ")
    senha = input("Crie uma senha de acesso: ").strip()

    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco, senha)
    clientes.append(cliente)

    print("Usuário cadastrado com sucesso!")

def criar_conta_corrente():
    global contador_conta
    print("\n--- Abertura de Conta Corrente ---")
    cpf = input("Informe o CPF do titular da conta: ").strip()

    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if cliente:
        conta = ContaCorrente(cliente, contador_conta)
        cliente.adicionar_conta(conta)
        print(f"Conta criada com sucesso! Número da conta: {contador_conta}")
        contador_conta += 1
    else:
        print("Usuário não encontrado. Cadastre o usuário antes de criar a conta.")

def selecionar_conta_por_senha():
    senha = input("Digite sua senha: ").strip()
    cliente = next((c for c in clientes if c.senha == senha), None)
    if not cliente:
        print("Senha incorreta ou cliente não encontrado.")
        return None

    if not cliente.contas:
        print("Cliente não possui contas.")
        return None

    if len(cliente.contas) > 1:
        print("Contas encontradas:")
        for i, conta in enumerate(cliente.contas):
            print(f"{i + 1} - Agência: {conta.agencia}, Número: {conta.numero}")
        escolha = int(input("Selecione o número da conta: "))
        return cliente.contas[escolha - 1]

    return cliente.contas[0]

def realizar_deposito():
    conta = selecionar_conta_por_senha()
    if not conta:
        return
    valor = float(input("Informe o valor do depósito: "))
    conta.depositar(valor)

def realizar_saque():
    conta = selecionar_conta_por_senha()
    if not conta:
        return
    valor = float(input("Informe o valor do saque: "))
    conta.sacar(valor)

def exibir_extrato():
    conta = selecionar_conta_por_senha()
    if not conta:
        return
    print("\n--- Extrato ---")
    if not conta.historico.transacoes:
        print("Nenhuma movimentação registrada.")
    else:
        for transacao in conta.historico.transacoes:
            print(transacao)
    print(f"\nSaldo atual: R$ {conta._saldo:.2f}")

def listar_contas():
    print("\n--- Contas Cadastradas ---")
    for cliente in clientes:
        for conta in cliente.contas:
            print(f"Titular: {cliente.nome} | Agência: {conta.agencia} | Conta: {conta.numero}")

def sistema_bancario():
    while True:
        print("""\n
O que deseja fazer?
1 - Fazer depósito
2 - Sacar dinheiro
3 - Ver extrato
4 - Criar usuário
5 - Criar conta corrente
6 - Listar contas
7 - Encerrar operação
        """)
        opcao = input("Escolha a opção: ").strip()

        if opcao == "1":
            realizar_deposito()
        elif opcao == "2":
            realizar_saque()
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            criar_usuario()
        elif opcao == "5":
            criar_conta_corrente()
        elif opcao == "6":
            listar_contas()
        elif opcao == "7":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema_bancario()
