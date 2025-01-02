# Cálculo de viagem

km = float(input("Quantos kms foram rodados? "))

# Define o preço baseado na distância
if km > 200:
    preco = km * 0.45
else:
    preco = km * 0.50

# Exibe o resultado
print("A sua viagem deu um total de {:.2f} kms. Valor a pagar: R$ {:.2f}".format(km, preco))
