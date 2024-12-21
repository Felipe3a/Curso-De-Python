import random
import emoji

# Sorteia um número entre 1 e 10
numS = random.randint(1, 10)

while True:
    # Solicita um número ao usuário
    num = int(input('Digite um número entre 1 e 10: '))

    # Verifica se o número está fora do intervalo válido
    if num < 1 or num > 10:
        print('Número inválido. Por favor, digite um número entre 1 e 10.')
        continue  # Reinicia o loop
    else:
        # Exibe o número escolhido e o número sorteado
        print('Número escolhido: {} | Número sorteado: {}'.format(num, numS))

        # Verifica se o número do usuário é igual ao número sorteado
        if num == numS:
            print(emoji.emojize('Parabéns, você foi sorteado! :star-struck:'))
        else:
            print(emoji.emojize('Que pena, não foi dessa vez. :pensive_face:'))
        break  # Sai do loop quando o número está válido e o jogo termina

