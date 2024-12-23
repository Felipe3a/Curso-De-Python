#----Programa que sortea a orden de  uma lista 


from random import choice


n1= input('Digite o 1° nome: ')
n2 = input('Digite o 2° nome: ')
n3 = input('Digite o 3° nome: ')
n4 = input('Digite o 4° nome: ')


lista = [n1,n2,n3,n4]

escolhido = choice(lista)

print( ' \nO nome sorteado foi {}\n'.format(lista))