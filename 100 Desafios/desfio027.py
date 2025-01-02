#------Programa que recebe um nome completo e retorna o primeiro e ultimo nome

nome = str(input('Digite o seu nome:')).strip()

fn = nome.split()


print('Ola seu primeiro nome é {}'.format(fn[0]))

print('E o seu ultimo nome é {}'.format(fn[len(fn)-1]))