import unicodedata

# Taxas de câmbio simuladas
taxas = {
    "BRL": {"USD": 0.20, "EUR": 0.18, "GBP": 0.15, "JPY": 30.00},
    "USD": {"BRL": 5.00, "EUR": 0.90, "GBP": 0.75, "JPY": 150.00},
    "EUR": {"BRL": 5.50, "USD": 1.11, "GBP": 0.83, "JPY": 160.00},
    "GBP": {"BRL": 6.70, "USD": 1.33, "EUR": 1.20, "JPY": 180.00},
    "JPY": {"BRL": 0.033, "USD": 0.0067, "EUR": 0.0062, "GBP": 0.0056}
}

# Mapeamento de nomes para códigos
nomes = {
    "real": "BRL", "dolar": "USD", "dólar": "USD", "euro": "EUR",
    "libra": "GBP", "iene": "JPY", "yen": "JPY", "ienes": "JPY", "yenes": "JPY"
}

def remover_acentos(txt):
    return ''.join(c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c) != 'Mn').lower()

def pegar_codigo(nome):
    return nomes.get(remover_acentos(nome))

def converter(valor, de, para):
    if de == para:
        return valor
    return valor * taxas.get(de, {}).get(para, 0)

def main():
    print("Moedas: REAL, DÓLAR, EURO, LIBRA, IENE")

    de = pegar_codigo(input("De: "))
    para = pegar_codigo(input("Para: "))
    if not de or not para:
        print("Moeda inválida.")
        return

    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("Valor inválido.")
        return

    resultado = converter(valor, de, para)
    print(f"{valor:.2f} {de} = {resultado:.2f} {para}")

if __name__ == "__main__":
    main()
