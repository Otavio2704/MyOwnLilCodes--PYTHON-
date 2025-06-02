# Lista para armazenar as tarefas
tarefas = []

# Função para mostrar o menu
def mostrar_menu():
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

# Função para adicionar uma tarefa
def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append({"descricao": tarefa, "concluida": False})
    print("\nTarefa adicionada com sucesso!")

# Função para mostrar as tarefas
def ver_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa na lista.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            status = "✅" if tarefa["concluida"] else "❌"
            print(f"{i}. {tarefa['descricao']} [{status}]")

# Função para marcar uma tarefa como concluída
def concluir_tarefa():
    ver_tarefas()
    try:
        numero = int(input("Digite o número da tarefa concluída: "))
        tarefas[numero - 1]["concluida"] = True
        print("Tarefa marcada como concluída!")
    except (IndexError, ValueError):
        print("Número inválido!")

# Função para remover uma tarefa
def remover_tarefa():
    ver_tarefas()
    try:
        numero = int(input("Digite o número da tarefa para remover: "))
        tarefas.pop(numero - 1)
        print("Tarefa removida!")
    except (IndexError, ValueError):
        print("Número inválido!")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        ver_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
