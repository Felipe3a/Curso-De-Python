# Programa que calcula o valor a ser pago pelo aluguel de um veículo



dias = int(input('Por quantos dias o carro foi alugado?'))
kmRod = float(input('Quantos  KM foram rodados?'))




diaria = 60
km = 0.15

total = (dias*diaria ) + (km * kmRod)

print('Número de diárias {}. Total díarias: R${:.2f}'.format(dias,diaria*dias))
print('Quilometros rodados {}. Total Quilometros: R${:.2f}.'.format(kmRod, kmRod*km))

print('Você utilizou o veículo por {} dias e rodou {} Km.\n  Total a pagar:R$ {:.2f} '.format(dias,kmRod,total))

