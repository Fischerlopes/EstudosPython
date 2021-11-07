#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista_mega = []
lista_jogos = []
total = 1
n = int(input('Quantos jogos você deseja fazer ? '))
while total <= n: # loop de acordo com a quantidade de jogos desejada pelo usuário
    count = 0
    while True: # loop para salvar o jogo, sem que haja repetição de dados
        num = randint(1,60)
        if num not in lista_mega:
            lista_mega.append(num)
            count += 1
        if count >= 6:
            break
    lista_mega.sort()#organizar a lista em ordem crescente
    lista_jogos.append(lista_mega[:]) # salvar a lista de jogos, sem criar relação com a lista anterior
    lista_mega.clear() # comando para não duplicar os dados da lista
    total += 1
print(lista_jogos)
for i, v in enumerate(lista_jogos): # for com chave e valor para impressão mais organizada
    print(v)
