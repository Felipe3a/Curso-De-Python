#----Programa que analisa uma quantas vezes a letra a aparece na frase

frase = str(input('Digite uma frase:')).upper().strip()

print('A letra A aparece {} vezes na frase {}'.format(frase.count('A'),frase))
print('Aletra A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez n posição {}'.format(frase.rfind('A')+1))