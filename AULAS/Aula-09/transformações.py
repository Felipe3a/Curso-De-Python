frase = 'Curso em Video Python'

# 1. Transformar para maiúsculas
maiuscula = frase.upper()  # Converte todos os caracteres para maiúsculas.

# 2. Transformar para minúsculas
minuscula = frase.lower()  # Converte todos os caracteres para minúsculas.

# 3. Capitalizar a string (primeira letra maiúscula e as demais minúsculas)
capitalizada = frase.capitalize()  # Converte a primeira letra para maiúscula e o resto para minúsculas.

# 4. Transformar para título (primeira letra de cada palavra maiúscula)
titulo = frase.title()  # Converte a primeira letra de cada palavra para maiúscula.

# 5. Transformar para maiúscula a primeira letra de cada palavra
inicial_maiuscula = frase.swapcase()  # Inverte o caso de cada caractere (maiúscula vira minúscula e vice-versa).

# 6. Substituir uma substring por outra
substituida = frase.replace('Python', 'Java')  # Substitui a palavra 'Python' por 'Java'.

# 7. Remover espaços à esquerda
sem_espaco_esquerda = frase.lstrip()  # Remove os espaços à esquerda da string.

# 8. Remover espaços à direita
sem_espaco_direita = frase.rstrip()  # Remove os espaços à direita da string.

# 9. Remover espaços à esquerda e à direita
sem_espacos = frase.strip()  # Remove os espaços em branco do início e do final da string.

# 10. Adicionar caracteres à esquerda até completar um comprimento
completa_esquerda = frase.zfill(30)  # Preenche com zeros à esquerda até a string atingir o comprimento 30.

# 11. Adicionar um prefixo
com_prefixo = frase.rjust(30, '*')  # Preenche com '*' à esquerda até a string atingir o comprimento 30.

# 12. Adicionar um sufixo
com_sufixo = frase.ljust(30, '-')  # Preenche com '-' à direita até a string atingir o comprimento 30.

# 13. Converter em uma lista de caracteres
lista_de_caracteres = list(frase)  # Converte a string em uma lista de caracteres.

# 14. Substituir uma palavra por outra, com limite de ocorrências
substituida_limite = frase.replace('o', 'O', 2)  # Substitui o 'o' por 'O', mas apenas as duas primeiras ocorrências.

# 15. Dividir a string em uma lista
dividida = frase.split()  # Divide a string em uma lista de palavras, usando o espaço como separador.

# 16. Dividir a string em uma lista com um delimitador específico
dividida_por_espacos = frase.split(' ')  # Divide a string usando o espaço como delimitador.

# 17. Verificar se a string está em minúsculas
verifica_minuscula = frase.islower()  # Verifica se todos os caracteres estão em minúsculas.

# 18. Verificar se a string está em maiúsculas
verifica_maiuscula = frase.isupper()  # Verifica se todos os caracteres estão em maiúsculas.

# 19. Remover os espaços internos
sem_espacos_internos = frase.replace(' ', '')  # Remove todos os espaços internos.

# 20. Trocar de posição a primeira e última letra
invertida = frase[::-1]  # Inverte toda a string.

# Exibindo as transformações
print("Maiúsculas:", maiuscula)
print("Minúsculas:", minuscula)
print("Capitalizada:", capitalizada)
print("Título:", titulo)
print("Inverter maiúsculas/minúsculas:", inicial_maiuscula)
print("Substituída:", substituida)
print("Sem espaço à esquerda:", sem_espaco_esquerda)
print("Sem espaço à direita:", sem_espaco_direita)
print("Sem espaços:", sem_espacos)
print("Completada à esquerda com zeros:", completa_esquerda)
print("Com prefixo:", com_prefixo)
print("Com sufixo:", com_sufixo)
print("Lista de caracteres:", lista_de_caracteres)
print("Substituída com limite:", substituida_limite)
print("Dividida:", dividida)
print("Dividida por espaços:", dividida_por_espacos)
print("Está em minúsculas?", verifica_minuscula)
print("Está em maiúsculas?", verifica_maiuscula)
print("Sem espaços internos:", sem_espacos_internos)
print("Inverta toda a string:", invertida)
