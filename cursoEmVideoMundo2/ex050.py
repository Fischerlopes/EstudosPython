#  Desenvolva um programa que leia seis números inteiros e
#  mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.
total= 0
for c in range(1, 7 ):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        total = total + num
    else:
        print('Esse número é impar, vamos desconsiderá-lo!')

print('A soma dos números pares é: {}'.format(total))

