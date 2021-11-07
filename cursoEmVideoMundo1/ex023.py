import math
a = int(input('Digite um número entre 0 e 9999 :'))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 % 10
print('Analisando o número {}'. format(a))
print('Unidade : {} '.format(u))
print('Dezena : {} '.format(d))
print('Centena :  {}'.format(c))
print('Milhar :  {}'.format(m))






