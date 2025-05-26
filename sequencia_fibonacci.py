#Função que gera a sequencia de fibonacci
def sequencia_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

# Menu
if __name__ == "__main__":
    termos = int(input("Quantos termos da sequência de Fibonacci você deseja? "))
    print(f"A sequência de Fibonacci com {termos} termos é: {sequencia_fibonacci(termos)}")
