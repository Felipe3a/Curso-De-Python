#----Programa que lê o nome de uma pesoa e diz se tem Silva no nome

nome = str(input('Digite seu nome: ')).strip()

print('SILVA' in nome.upper())