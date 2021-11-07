import math
num = float(input('Digite um número: '))
raiz = int(round(math.ceil(num), 0))
print('O valor digitado foi: {}, e o número inteiro é : {}'.format(num, raiz))