from datetime import datetime, timedelta

#Menu principal
def menu():
    print("\nCalculadora de Dias")
    print("1. Somar dias a uma data")
    print("2. Subtrair dias de uma data")
    print("3. Sair")

#Obtém a data oferecida pelo usuário
def obter_data():
    data_str = input("Digite a data no formato (DD/MM/AAAA): ")
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data
    except ValueError:
        print("Data inválida. Tente novamente.")
        return obter_data()

#Obtém os dias oferecidos pelo usuário
def obter_dias():
    try:
        dias = int(input("Digite o número de dias: "))
        return dias
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return obter_dias()

#Menu principal
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = obter_data()
            dias = obter_dias()
            nova_data = data + timedelta(days=dias)
            print(f"Data resultante: {nova_data.strftime('%d/%m/%Y')}")
        elif opcao == "2":
            data = obter_data()
            dias = obter_dias()
            nova_data = data - timedelta(days=dias)
            print(f"Data resultante: {nova_data.strftime('%d/%m/%Y')}")
        elif opcao == "3":
            print("Saindo da calculadora.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
