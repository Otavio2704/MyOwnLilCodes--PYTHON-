import unicodedata

# Taxas de câmbio simuladas
taxas = {
    "BRL": {"USD": 0.18, "EUR": 0.16, "GBP": 0.13, "JPY": 26.00},
    "USD": {"BRL": 5.64, "EUR": 0.89, "GBP": 0.75, "JPY": 146.70},
    "EUR": {"BRL": 6.31, "USD": 1.12, "GBP": 0.84, "JPY": 163.97},
    "GBP": {"BRL": 7.48, "USD": 1.33, "EUR": 1.19, "JPY": 194.57},
    "JPY": {"BRL": 0.038, "USD": 0.0068, "EUR": 0.0061, "GBP": 0.0051}
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
