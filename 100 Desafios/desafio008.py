# Programa que lê um valor e o exibe convertido em metros e centimtros


print("Conversor de metros para centímetros e milímetros")
valor_metros = int(input("Digite o valor em metros: "))  # Usando int para valores inteiros

# Conversões
valor_centimetros = valor_metros * 100  # 1 metro = 100 cm
valor_milimetros = valor_metros * 1000  # 1 metro = 1000 mm

# Saída formatada
print(f"O valor de {valor_metros} metros corresponde a:")
print(f"{valor_centimetros} centímetros")
print(f"{valor_milimetros} milímetros")
