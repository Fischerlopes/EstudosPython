#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
a = randint(1,4)
count = 0

print('-= ' * 10 + 'Jogo de Advinhação' + '-= ' * 10 )
b = int(input('Digite seu número: '))
while a != b:
    c = print('Verificando: 3...')
    sleep(1)
    c = print('Verificando: 2...')
    sleep(1)
    c = print('Verificando: 1...')
    sleep(1)
    b = int(input('hhuumm quase lá, tente novamente! Qual o seu número ? '))
    count += 1

print('Você acertou' if a == b else 'Você errou')
print(f'Você precisou usar {count} palpite(s)')


