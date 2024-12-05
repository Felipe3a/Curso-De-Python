import random
numS = random.randint(1, 10)

num = int(input('Digite um número entre 1 e 10: '))

print('Número escolhido {} número sorteado {}'.format(num, numS))

if num == numS:
    print('Parabéns você foi sorteado!')

else : print('Que pena não foi dessa vez')