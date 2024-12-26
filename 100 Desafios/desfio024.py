# ------Programa que verifica so o nome da cidade começa com santo ouu não


cit = str(input('Em que cidade voê nasceu? ')).strip() #strip elimina os espaços nop inicio e no fim


print(cit[:5].upper() == 'SANTO')
