import time
import random

print(' === JOGO JOKENPO === ')
print(''' ESCOLHA SUA OPCÃO 
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA''')
jogador = int(input('Qual é a sua jogada ? '))

print('Vamos ao jogo!!')
time.sleep(1)
print('Jo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('Po')

list = ['Pedra','Papel','Tesoura']

computador = random.choice(list)

if jogador == 1 and computador == 'Papel':
    print('O Computador jogou: {}'.format(computador))
    print('Você jogou: Pedra')
    print('O computador venceu')
elif jogador == 2 and computador == 'Tesoura':
    print('O Computador jogou: {}'.format(computador))
    print('Você jogou: Papel')
    print('O computador venceu')
elif jogador == 3 and computador == 'Pedra':
    print('O Computador jogou: {}'.format(computador))
    print('Você jogou: Tesoura')
    print('O computador venceu')
elif jogador == 1 and computador == 'Tesoura':
    print('O Computador jogou: {}'.format(computador))
    print('Você jogou: Pedra')
    print('O jogador venceu')
elif jogador == 3 and computador == 'Papel':
    print('O Computador jogou: {}'.format(computador))
    print('Você jogou: Tesoura')
    print('O jogado venceu')
elif jogador == 2 and computador == 'Pedra':
    print('O Computador jogou: {}'.format(computador))
    print('Você jogou: Papel')
    print('O jogador venceu')
else:
    print('O Computador jogou: {}'.format(computador))
    print('Você jogou: {}'.format(computador))
    print('Empate - Joque novamente')
