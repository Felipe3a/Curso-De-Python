
# outra maneira de fazer usndo apena sqrt de math


from math import sqrt,floor  #Dessamaneira estamos importando somente a o metodo sqrt que é o método para calcular a raiz quadrada
num = int(input('Digite um número: '))

raiz = sqrt(num)

print ('A raiz de {} é igual a {:.1f}'.format(num,raiz))