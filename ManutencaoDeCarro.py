from datetime import datetime, timedelta

tipo_carro = input('Qual o tipo do seu carro (P/M/G)?: ')  # Tipo de carro: Pequeno, Médio, Grande
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now().date()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(days=tempo_grande)
    print(f"O carro chegou às: {data_atual} e ficará pronto às {data_estimada}")
