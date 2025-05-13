def sequencia_fibonacci(n):
    """
    Gera a sequência de Fibonacci até o n-ésimo termo.
    
    :n: Número de termos da sequência.
    :return: Uma lista contendo a sequência de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Exemplo de uso
if __name__ == "__main__":
    termos = int(input("Quantos termos da sequência de Fibonacci você deseja? "))
    print(f"A sequência de Fibonacci com {termos} termos é: {sequencia_fibonacci(termos)}")
