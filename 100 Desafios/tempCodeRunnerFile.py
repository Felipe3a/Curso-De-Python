# Programa que recebe 3 retas e diz se elas podem formar um triangulo

r1 = float(input('Qual o tamnho da primeira reta? '))
r2 = float(input('Qual o tamnho da segunda reta? '))
r3 = float(input('Qual o tamnho da terceira reta? '))

soma = r1 + r2


if r3 < soma:
    print('Forma um triangulo!')
else:
    print('Não forma um triangulo!')


