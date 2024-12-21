# Importando bibliotecas , no exemplo abaixo estamos importando a biblioteca math, que siguinifica matemática


import math  # dessa maneira estamos importando todos o métodos matemáticos
num = int(input('Digite um número: '))

raiz = math.sqrt(num)  # Método para calcular a raiz quadrada

print('A raiz de {} é igual a {:.1f}'.format(num, raiz))
