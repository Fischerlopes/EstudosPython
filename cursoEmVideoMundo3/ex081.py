#: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados. lista de valores, ordenada de forma decrescente.
# # C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = str(input('Quer digitar um número ? [S/N]')).strip()[0]
    if n in 'sS':
        lista.append(int(input('Digite um número: ')))
    else:
        break

print(f'Você digitou {len(lista)} números')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não está na lista')




