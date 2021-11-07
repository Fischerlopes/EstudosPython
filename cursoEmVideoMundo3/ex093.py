# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
tot = 0
jogador['nome'] = str(input('Nome do jogador: '))
print(jogador)
n = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(1,n + 1):
  g = int(input(f'Quantos gols na partida {c} ? '))
  gols.append(g)
tot = sum(gols)
jogador['gols'] = gols
jogador['Total'] = tot
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k , v in jogador.items():
  print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} fez {n} partidas')
for k, v in enumerate(jogador['gols']):
  print(f' ==> Na partida {k}, fez {v} gols')