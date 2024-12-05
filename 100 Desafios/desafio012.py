# Agoritimo que lê o preço de um produto e da um desconto de 5%


preço = int(input('Digite o valor do produto:'))



newPreço = preço - (preço *5/100)


print('O valor com desconto é: R$ {:.2f} '.format(newPreço))
