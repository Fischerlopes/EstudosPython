# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

list = []
termo = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
quantidade = int(input('Digite a quantidade de iterações que você deseja: '))
repeticao = termo + (quantidade -1) * razao
for c in range(termo, repeticao + razao, razao):
    print('{}'.format(c), end='-> ')
