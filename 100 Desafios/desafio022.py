# Programa que lê o nome de uma pessoa e mostra:
# - O nome com todas as letras maiúsculas;
# - O nome com todas as letras minúsculas;
# - Quantas letras tem ao todo (desconsiderando espaços);
# - Quantas letras tem o primeiro nome.

nome_completo = input('Digite seu nome:  ')  # Solicita o nome completo do usuário.

# Transforma todas as letras do nome em maiúsculas.
maiúsculas = nome_completo.upper()

# Transforma todas as letras do nome em minúsculas.
minusculas = nome_completo.lower()

# Divide o nome em palavras e seleciona o primeiro nome.
primeiro_nome = nome_completo.split()[0]

# Remove todos os espaços do nome completo.
nome_sem_espacos = nome_completo.replace(" ", "")

# Conta o total de caracteres do nome sem espaços.
tot = len(nome_sem_espacos)

# Conta o total de letras no primeiro nome.
tot_primeiro_nome = len(primeiro_nome)

# Imprime os resultados formatados.
print('Maiúsculas: {}'.format(maiúsculas))
print('Minúsculas: {}'.format(minusculas))
print('Seu nome tem {} letras ao total.'.format(tot))
print('Primeiro nome: {}'.format(primeiro_nome))


# Veja outra maneira mais simplificada de fazer o mesmo:

nome_completo = str(input('Digite seu nome: ')).strip()  # Recebe o nome e remove os espaços no início e no final.

# Imprime o nome com todas as letras em maiúsculas.
print('Maiúsculas: {}'.format(nome_completo.upper()))

# Imprime o nome com todas as letras em minúsculas.
print('Minúsculas: {}'.format(nome_completo.lower()))

# Calcula o total de letras no nome (desconsiderando espaços) e imprime.
print('Seu nome tem {} letras ao total.'.format(len(nome_completo) - nome_completo.count(' ')))

# Divide o nome em palavras, seleciona e imprime o primeiro nome.
print('Primeiro nome: {}'.format(nome_completo.split()[0]))

# Encontra o índice do primeiro espaço e imprime (equivalente ao número de letras do primeiro nome, se houver um espaço).
print('Seu primeiro nome tem {} letras.'.format(nome_completo.find(' ')))
