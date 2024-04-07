import random

letras = 'qwertyuioplkjhgfdsamnbvcxz'
numeros = '123456789'
caracteres_especiais = '!@#$%¨&*'


todos_os_caracteres = letras + numeros + caracteres_especiais

tamanho_da_senha = int(input("Digite o tamanho desejado para a senha: "))

senha = ''.join(random.choice(todos_os_caracteres) for i in range(tamanho_da_senha))


print(f"Senha gerada: {senha}")
