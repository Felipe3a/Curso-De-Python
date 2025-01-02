import emoji
import random
import time

# Faz o computador escolher um número entre 1 e 5
print('=='*50)
print('\nVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\nPensando', end='', flush=True)

# Efeito de carregamento com os três pontinhos aparecendo um a um
for _ in range(3):
    print('.', end='', flush=True)  # Aparece um ponto
    time.sleep(0.5)  # Espera meio segundo

# Continuar a mostrar os pontos em loop até o usuário digitar a resposta
for _ in range(3):  # A repetição do efeito de carregamento
    print('.', end='', flush=True)
    time.sleep(0.5)
   
# Solicita a resposta do usuário
print('\n')

print('=='*50) 
n = int(input('\nEm que número eu pensei? '))

# Computador escolhe um número aleatório
numero = random.randint(0, 5)

# Verifica se o usuário acertou ou errou
if numero == n:
    print(emoji.emojize('\n:pensive_face:  Perdi eu pencei no número {} e você digitou o número {}\n5'.format(numero, n)))
else:
    print(emoji.emojize('\n:grinning_face: Ganhei, eu pencei no número {} e você digitou o número {}\n'.format(numero, n)))



