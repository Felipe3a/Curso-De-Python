# -------Programa que recebe um um número  de 0 a 9999 e mostra na tela os digitos separados

num = int(input('Digite um Número de 0 a 9999:'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analizando o número {}'.format(num))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
