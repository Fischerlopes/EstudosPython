tupla = (int(input('Digite um número: ')), int(input('Digite um número:')),
         int(input('Digite um número: ')),int(input('Digite um número: ')))
print(f'Você digitou os seguintes valores: {tupla}')
print(f'O número 9, apareceu {tupla.count(9)} vezes')
print(f'O valor 3 apareceu na {tupla.index(3)}a posição')
n = 0
for c in tupla:
    if c % 2 == 0:
        n += 1
print(f'Você digitou {n} números pares')