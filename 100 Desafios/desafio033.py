# -- Programa que recebe 3 números e diz qual é o menor e qual é o menor

n1 = int(input('Digite o número: '))
n2 = int(input('Digite o número: '))
n3 = int(input('Digite o número: '))

menor = n1


if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3


maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O número {} é o menor e  o número {} é o maior'.format(menor, maior))
