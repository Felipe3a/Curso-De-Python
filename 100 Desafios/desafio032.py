#--Programa que mostra se o ano é bissexto ou não
from datetime import date #vbiblioteca que de data
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year # busca o ano atual


if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))