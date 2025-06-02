from datetime import datetime

#Classe do cliente
class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return f"{self.nome} (CPF/CNPJ: {self.documento})"

#Classe dos produtos
class Produto:
    def __init__(self, nome, preco_unitario):
        self.nome = nome
        self.preco_unitario = preco_unitario

    def __str__(self):
        return f"{self.nome} - R$ {self.preco_unitario:.2f}"

#Classe dos itens da nota fiscal
class ItemNota:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco_unitario * self.quantidade

    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade} - R$ {self.subtotal():.2f}"


#Classe da nota fiscal
class NotaFiscal:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.data = datetime.now()

    def adicionar_item(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        item = ItemNota(produto, quantidade)
        self.itens.append(item)

    def total(self):
        return sum(item.subtotal() for item in self.itens)

    def imprimir(self):
        print("\n========== NOTA FISCAL ==========")
        print(f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}")
        print(f"Cliente: {self.cliente}")
        print("\nItens:")
        for item in self.itens:
            print(f"  - {item}")
        print(f"\nTOTAL: R$ {self.total():.2f}")
        print("=================================\n")


#Menu da nota fiscal
def main():
    print("=== Gerador de Nota Fiscal ===")
    nome = input("Nome do cliente: ")
    documento = input("CPF ou CNPJ: ")
    cliente = Cliente(nome, documento)
    nota = NotaFiscal(cliente)

    while True:
        print("\n--- Novo Produto ---")
        nome_produto = input("Nome do produto: ")
        try:
            preco = float(input("Preço unitário (R$): "))
            quantidade = int(input("Quantidade: "))
            if preco < 0 or quantidade <= 0:
                print("Preço e quantidade devem ser positivos.")
                continue
        except ValueError:
            print("Valores inválidos. Tente novamente.")
            continue

        produto = Produto(nome_produto, preco)
        nota.adicionar_item(produto, quantidade)

        continuar = input("Adicionar outro produto? (s/n): ").lower()
        if continuar != 's':
            break

    nota.imprimir()


if __name__ == "__main__":
    main()
