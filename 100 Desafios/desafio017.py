# -------Programa que lê o comprimento do cateto oposto e do cateto adjacente de um triangulo e mostra o comprimento da ipotenusa.




  #---Maneira de fazer sem a importação de biblioteca--------
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi =  (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medit {:.2f}'.format(hi))


#-------Maneira de fazer importando a biblioteca mth----------


from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi =  hypot(co, ca)    # Veja como simplifica e facilita o calculo da hipotenusa
print('A hipotenusa vai medit {:.2f}'.format(hi))