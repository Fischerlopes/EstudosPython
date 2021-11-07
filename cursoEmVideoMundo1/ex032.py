from datetime import date

a = int(input('Digite o ano que você quer analisar: Digite 0 para o ano atual '))

if a == 0:
    a = date.today().year

print('O ano: {} é Bissexto'.format(a) if a % 4 == 0 and a % 100 != 0 else 'O ano: {} não é Bissexto'.format(a))

