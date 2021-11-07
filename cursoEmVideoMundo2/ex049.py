#  Refaça o DESAFIO 9, mostrando a tabuada de um
#  número que o usuário escolher, só que agora utilizando um laço for.

a = int(input('Escolha qual tabuada você quer calcular:'))
print('A tabuada de {} é : '.format(a))
print('==' * 10)
for c in range(0, 11):
    print('{} x {} = {}'.format(c, a,  c * a))