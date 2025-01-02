#Programa que multa se o carro ultrapssar a velocidade maxima de 80 km/h


v = float(input('Velocidade do veículo? '))

limite = 80
excesso = v - limite
multa = excesso * 7

print('\nVelocidade maxima permitida {:.0f} km/h.\n\nVelocidade registrada {:.0f} km/h.'.format(limite, v))

if v > limite:
       print('\nVocê foi  multado!\nValor da multa: R$ {:.2f}'.format(multa))
else:
       print('\nTenha um bom dia e dirija com segurança!\n')


