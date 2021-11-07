#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

list = []
mai = men = 0
# adicionar os números na lista
for c in range(0,5):
    list.append(int(input(f'Digite o número na posição {c}: ')))
# fazer compartivo do menor e mario valores para salvar numa variável, dessa forma não precisa criar outra lista
    if c == 0:
        mai = men = list[0]
    else:
        if list[c] > mai:
            mai = list[c]
        if list[c] < men:
            men = list[c]


print(f'Os valores digitados foram: {list}')
print(f'O maior valor digitado foi: {mai}, nas posições:', end='')
#usando um for , chamando a posição na lista para imprimir a posição dos maiores e menores valores.
for i, v in enumerate(list):
    if v == mai:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi: {men}, nas posições: ', end='')
for i, v in enumerate(list):
    if v == men:
        print(f'{i}...', end='')

