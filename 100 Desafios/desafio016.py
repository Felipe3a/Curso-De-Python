# Programa que recebe um número e  mostra sua porção inteira


# ---------------Importando a biblioteca math inteira-------------
from math import trunc
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua prção inteira é {}'.format(num, math.trunc(num)))


# ---------------Immportando apenas trunc de math --------------------


num = float(input('Digite um número: '))


numInt = trunc(num)



#------- A baixo veja oiutra maneir de fazer sem importar nenhuma biblioteca---------------


num = float(input('Digite um número: '))
print('O valor digitado foi {}, e sua porção inteira é {}.'.format(num, int(num)))