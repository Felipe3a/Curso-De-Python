# algoritimo que recebe um número e mostra o seu dobro, triplo e a sua raiz quadrada


n = int(input('Digite um  número:'))

d = n*2
t = n*3
r = n**0.5

print('O dobro de {} é {},\n  o triplo é {} e a sua raiz quadrada é {:.2f}'.format(n,d, t, r))
