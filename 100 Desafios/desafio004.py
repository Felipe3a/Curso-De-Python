# Programa que lê o dado e retorna o tipo desse dado


n = input('Digite algo: ')

print('{} é uma letra?'.format(n), n.isalpha())

print('{} é um número?'.format(n), n.isnumeric())


print('{} é um decimal?'.format(n), n.isdecimal())


