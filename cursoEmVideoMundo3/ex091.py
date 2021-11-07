#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
jogo_dados = dict()

for j in range(0,4):
  jogo_dados[j] = randint(1,6)

print(jogo_dados)
#fazer o dicionário com os 04 jogadores
jogo_completo = {'Jogador 1': randint(1,6),
                 'Jogador 2': randint(1,6),
                 'Jogador 3': randint(1,6),
                 'Jogador 4':randint(1,6) }
for k, v in jogo_completo.items():
  print(f'{k} tirou {v} no dado.')
ranking = list()
ranking = sorted(jogo_completo.items(), key = itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
  print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')