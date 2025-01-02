r1 = float(input('Qual o tamanho da primeira reta? '))
r2 = float(input('Qual o tamanho da segunda reta? '))
r3 = float(input('Qual o tamanho da terceira reta? '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Forma um triangulo!')
else:
    print('Não forma um triangulo!')
