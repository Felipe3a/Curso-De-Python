
print('--Programa 01--')
tempo = int(input('Qa=uantoa anos tem o seu carro? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim programa 01')

print('--Programa 02--')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segubda nota'))

media = (n1 + n2) / 2


if media <= 6:
    print('Sua mèdia esta baixa')
else:
    print('Sua média eastá boa, parabens')  

print('Parabéns!'if media <=6 else 'Estude mais!')  
print('--Fim programa 02--')