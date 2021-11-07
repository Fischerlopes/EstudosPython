intNumber = int(input('Digite um número: '))
print('=*=*' * 10)
print('Escolha qual base você quer converter: ')
print('=-=-' * 10)
print('[ 1 ] - Binário')
print('[ 2 ] - Octal')
print('[ 3 ] - Hexadecimal')

baseConversion = int(input('1 / 2 / 3 : '))

if baseConversion == 1:
    print('O número {} na base Binária é : {}'.format(intNumber, bin(intNumber) [2:]))
elif baseConversion == 2:
    print('O número {} na base Octogonal é : {}'.format(intNumber, oct(intNumber)[2:]))
else :
    print('O número {} na base Hexadecimal é : {}'.format(intNumber, hex(intNumber)[2:]))



