# analisando triângulos

a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('Com essas informações, é possível montar um triângulo', end=' ')
    if a == b == c:
        print('Equilátero')
    if a != b != c != a:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Com essas informações, NÃO é possível montar um triângulo')
