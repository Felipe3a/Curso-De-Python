# Programa que calcula o valor do aumento de salário

salario = float(input("Qual o valor do salário? "))

if salario > 1250:
    aumento = salario + (salario * 0.10)
    print(f"O seu salário é R$ {salario:.2f}. Com o aumento de 10%, vai para R$ {aumento:.2f}.")
else:
    aumento = salario + (salario * 0.15)
    print(f"O seu salário é R$ {salario:.2f}. Com o aumento de 15%, vai para R$ {aumento:.2f}.")
