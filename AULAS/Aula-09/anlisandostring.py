
frase = 'Curso em Video Python'

# 1. Tamanho da string
tamanho = len(frase)  # Retorna o número de caracteres da string.

# 2. Contagem de uma substring específica
quantidade_o = frase.count('o')  # Conta quantas vezes o caractere 'o' aparece na string.

# 3. Contagem de uma substring específica
quantidade_de = frase.count('de')  # Conta quantas vezes a frase 'de' aparece.

# 4. Encontrar a posição de uma substring
posicao_de = frase.find('deo')  # Retorna a posição onde a substring 'deo' aparece pela primeira vez.

# 5. Verificar a existência de uma substring
contém_video = 'Video' in frase  # Verifica se a substring 'Video' está na string.

# 6. Verificar se a string começa com um prefixo
começa_com_curso = frase.startswith('Curso')  # Verifica se a string começa com 'Curso'.

# 7. Verificar se a string termina com um sufixo
termina_com_python = frase.endswith('Python')  # Verifica se a string termina com 'Python'.

# 8. Verificar se todos os caracteres são alfabéticos (sem números ou espaços)
apenas_letras = frase.isalpha()  # Retorna True se todos os caracteres forem letras.

# 9. Verificar se a string contém apenas dígitos
apenas_digitos = frase.isdigit()  # Retorna True se todos os caracteres forem dígitos.

# 10. Verificar se a string contém apenas espaços
só_espacos = frase.isspace()  # Retorna True se a string for composta apenas por espaços.

# 11. Verificar se todos os caracteres estão em maiúsculas
está_maiuscula = frase.isupper()  # Retorna True se todos os caracteres estiverem em maiúsculas.

# 12. Verificar se todos os caracteres estão em minúsculas
está_minuscula = frase.islower()  # Retorna True se todos os caracteres estiverem em minúsculas.

# Exibindo os resultados das análises
print(f"Tamanho da string: {tamanho}")
print(f"Contagem da letra 'o': {quantidade_o}")
print(f"Contagem da substring 'de': {quantidade_de}")
print(f"Posição da substring 'deo': {posicao_de}")
print(f"A string contém 'Video': {contém_video}")
print(f"A string começa com 'Curso': {começa_com_curso}")
print(f"A string termina com 'Python': {termina_com_python}")
print(f"A string contém apenas letras? {apenas_letras}")
print(f"A string contém apenas dígitos? {apenas_digitos}")
print(f"A string contém apenas espaços? {só_espacos}")
print(f"A string está em maiúsculas? {está_maiuscula}")
print(f"A string está em minúsculas? {está_minuscula}")
