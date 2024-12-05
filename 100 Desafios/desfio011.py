# Programa que calcula a quantidade de tinta necessária  para pinitar uma parede




alt = float(input('Qual é a altura do local a ser pintado? '))

larg = float(input('Qual e a largura do local a ser pintado? '))


area = alt * larg

tin = area/2

print('a dinmençao do local a ser pintado é de {}x{} e sua área é de {}m².'.format(alt, larg, area))


print('Serão necessários {} litros de tinta'.format(tin))


