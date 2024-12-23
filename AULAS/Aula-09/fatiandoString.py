

# Fatiamento


# Exemplo 1: Fatiamento básico
frase = 'Curso em Video Python'

# Pegar os 5 primeiros caracteres
f1 = frase[:5]
print(f1)  # 'Curso'

# Pegar os caracteres do índice 5 até o 8
f2 = frase[5:9]
print(f2)  # ' em '

# Pegar os caracteres do índice 9 até o final
f3 = frase[9:]
print(f3)  # 'Video Python'

# Exemplo 2: Usando passo no fatiamento
# Pegar a string do início até o fim, mas com passo 2 (pega a cada 2 caracteres)
f4 = frase[::2]
print(f4)  # 'Cr emVdo yhn'

# Pegar do início até o índice 10, com passo 3
f5 = frase[:11:3]
print(f5)  # 'C eV'

# Pegar do índice 9 até o final, com passo 4
f6 = frase[9::4]
print(f6)  # 'Vh'

# Exemplo 3: Fatiamento com valores negativos (passo negativo)
# Inverter a string inteira (passo -1)
f7 = frase[::-1]
print(f7)  # 'nohtyP odiV me osruC'

# Pegar a string do final até o índice 5 (em ordem reversa)
f8 = frase[15:5:-1]
print(f8)  # 'nohtyP odi'

# Pegar a string do final até o índice 10, com passo -2
f9 = frase[14:9:-2]
print(f9)  # 'yVd'

# Exemplo 4: Fatiamento com valores negativos para índices de início e fim
# Pegar os últimos 5 caracteres
f10 = frase[-5:]
print(f10)  # 'thon'

# Pegar do penúltimo caractere até o 7º, com passo 2
f11 = frase[-2:-8:-2]
print(f11)  # 'yVd'

# Pegar os 3 primeiros caracteres em ordem reversa (início negativo)
f12 = frase[:-15:-1]
print(f12)  # 'C'

# Exemplo 5: Fatiamento com valores fora do intervalo
# Tentar pegar uma parte da string com índices fora do intervalo
# Não existe esse intervalo na string, então retorna uma string vazia
f13 = frase[20:25]
print(f13)  # ''

# Iniciar o fatiamento de um índice negativo grande, como -30, que está fora do intervalo da string
f14 = frase[-30:-25]
print(f14)  # ''

# Exemplo 6: Fatiamento com valores de início e fim iguais
# Fatiamento onde o início e fim são iguais (resulta em uma string vazia)
f15 = frase[7:7]
print(f15)  # ''

# Iniciar do índice 5 e terminar no índice 5 (também retorna uma string vazia)
f16 = frase[5:5]
print(f16)  # ''

# Exemplo 7: Fatiamento com valores de passo negativo e índices grandes
# Começar do final e pegar uma parte da string em ordem reversa
f17 = frase[-10:-15:-1]
print(f17)  # 'deoV'

# Começar do final e pegar em ordem reversa até o início
f18 = frase[::-3]
print(f18)  # 'n oVe o'

# Exemplo 8: Fatiamento para pegar substrings específicas
# Pegar a palavra 'Video' que começa no índice 9 e vai até o índice 14
f19 = frase[9:14]
print(f19)  # 'Video'

# Pegar a palavra 'Python' que começa no índice 15 e vai até o final
f20 = frase[15:]
print(f20)  # 'Python'
