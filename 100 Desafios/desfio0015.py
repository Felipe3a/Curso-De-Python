# Programa que calcula o valor a ser pago pelo aluguel de um veículo



dias = int(input('Por quantos dias o carro foi alugado?'))
kmIncial = float(input('KM inicial:'))
kmFinal =float(input('Km final:'))

quantidadeKm = kmFinal - kmIncial

diaria = 60
km = 0.15

total = (dias*diaria ) + (km * quantidadeKm )

print('Número de diárias {}. Total díarias: R${:.2f}'.format(dias,diaria*dias))
print('Quilometros rodados {}. Total Quilometros: R${:.2f}.'.format(quantidadeKm , quantidadeKm *km))

print('Você utilizou o veículo por {} dias e rodou {} Km.\n  Total a pagar:R$ {:.2f} '.format(dias,quantidadeKm ,total))

