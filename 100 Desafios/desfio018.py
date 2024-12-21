# ------Programam que lê um ângulo e mostra na tela  o valor do seno, cosseno e a tangente desse ângulo.
import math


an = float(input('Digite o angulo: '))
seno = math.sin(math.radians(an))

print('O ângulo de {} tem o Seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(an, cosseno))
tang = math.tan(math.radians(an))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(an, tang))


# --------outra maneira  mais simples de fazer --------


 
from math import sin,cos,tan,radians


an = float(input('Digite o angulo: '))
seno = sin(radians(an))

print('O ângulo de {} tem o Seno de {:.2f}'.format(an, seno))
cosseno =  cos(radians(an))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(an, cosseno))
tang = tan(radians(an))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(an, tang))