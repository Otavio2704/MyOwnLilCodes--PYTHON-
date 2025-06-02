import random
import string

tamanho = 10  # tamanho da senha

# Letras (maiúsculas e minúsculas), números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
print(senha)
