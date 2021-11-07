a = input('Digite seu nome: ')
print('O seu nome em letras maiúsculas é: {} '.format(a.upper()))
print('O seu nome em letras minúsculas é: {} '.format(a.lower()))

print('Seu nome tem {} letras!'.format(len(a.replace(' ',''))))

b = a.split()
print('Seu primeiro nome tem {} letras'.format(len(b[0])))



