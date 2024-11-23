''' Tipos primiticos

• int : numéros inteiros. Ex; 7   -4    0   1365

• float  numéros flutuantes ou número real. Ex;  4.5     0.555   -15.555   7.0

• boll   Só aceita 2 valores  True ou False    sempre comece com letras maiúsculas

• str   Palavras. Ex 'Olá', '7.5'   ''   lembre-se de sempre usar aspas!




'''


n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

s = n1 + n2



# comandos com a mesma sída


#-----------------------------------------------------------------------------------
print(' A soma vale: ', s)               

print(' A soma vale: {}'.format(s))
#-------------------------------------------------------------------------------------------

print('A soma entre {}'.format(n1) + ' e {}'.format(n2) +' é {}'.format(s))


print('A soma entre {} e {}  vale {}'.format(n1.n2,s)) # os dois comandos tem a mesma saída, o segundo tem a melhor prática