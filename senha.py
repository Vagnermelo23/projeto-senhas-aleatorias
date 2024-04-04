import random

# Define os conjuntos de caracteres
letras = 'qwertyuioplkjhgfdsamnbvcxz'
numeros = '123456789'
caracteres_especiais = '!@#$%¨&*'

# Combina todos os conjuntos de caracteres
todos_os_caracteres = letras + numeros + caracteres_especiais

# Solicita o tamanho da senha ao usuário
tamanho_da_senha = int(input("Digite o tamanho desejado para a senha: "))

# Gera a senha aleatória
senha = ''.join(random.choice(todos_os_caracteres) for _ in range(tamanho_da_senha))

# Exibe a senha gerada
print(f"Senha gerada: {senha}")
