# leitura ano e classificação com 05 variáveis

from datetime import date
atual = date.today().year
anonasc = int(input('Digite seu ano de nascimento: '))
difyear = atual - anonasc
if difyear >= 25: print('O atleta tem {} anos *** Classifação: Master'.format(difyear))
elif difyear >= 19 and difyear < 25: print('O atleta tem {} anos *** Classifação: Senior'.format(difyear))
elif difyear >= 14 and difyear < 19: print('O atleta tem {} anos *** Classifação: Júnior'.format(difyear))
elif difyear >= 9 and difyear < 14: print('O atleta tem {} anos *** Classifação: Mirim'.format(difyear))
else: print('O atleta tem {} anos *** Classifação: Infantil'.format(difyear))