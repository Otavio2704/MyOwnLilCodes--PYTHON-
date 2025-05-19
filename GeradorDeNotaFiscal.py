from datetime import datetime

class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return f"{self.nome} (CPF/CNPJ: {self.documento})"


class Produto:
    def __init__(self, nome, preco_unitario):
        self.nome = nome
        self.preco_unitario = preco_unitario

    def __str__(self):
        return f"{self.nome} - R$ {self.preco_unitario:.2f}"


class ItemNota:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco_unitario * self.quantidade

    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade} - R$ {self.subtotal():.2f}"


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
        print("========== NOTA FISCAL ==========")
        print(f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}")
        print(f"Cliente: {self.cliente}")
        print("\nItens:")
        for item in self.itens:
            print(f"  - {item}")
        print(f"\nTOTAL: R$ {self.total():.2f}")
        print("=================================")


# === Exemplo de uso ===

cliente = Cliente("João Silva", "123.456.789-00")
produto1 = Produto("Mouse Gamer", 150.00)
produto2 = Produto("Teclado Mecânico", 250.00)

nota = NotaFiscal(cliente)
nota.adicionar_item(produto1, 2)
nota.adicionar_item(produto2, 1)

nota.imprimir()
