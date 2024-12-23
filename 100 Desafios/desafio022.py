# Programa que lê o nome de uma pessoa e mostra o nome com todas as letras maiúsculas, o nome com todas as letras minúsculasa, quantas letras tem ao todo espaços, quantas letras tem o primeiro nome


nome_completo = input('Digite seu nome:  ')

# Transforma todas as letras em maiúsculas
maiúsculas = nome_completo.upper()

# Transforma todas as letras em minúsculas
minusculas = nome_completo.lower()

primeiro_nome = nome_completo.split()[0]

# Removendo espaços extras em todo o nome
nome_sem_espacos = nome_completo.replace(" ", "")  # Remove todos os espaços
tot = len(nome_sem_espacos)  # Conta os caracteres sem espaços


# Imprime os resultados
print("Maiúsculas:", maiúsculas)
print("Minúsculas:", minusculas)
print("Total de caracteres (sem espaços):", tot)
print('primeiro nome: ',Primeiro_nome)
