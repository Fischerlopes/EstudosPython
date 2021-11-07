# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
gols = list()
tot = 0
time = list()
while True:
  jogador.clear()
  jogador['nome'] = str(input('Nome do jogador: '))
  print(jogador)
  n = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
  gols.clear()
  for c in range(1,n + 1):
    g = int(input(f'Quantos gols na partida {c} ? '))
    gols.append(g)
  tot = sum(gols)
  jogador['gols'] = gols
  jogador['Total'] = tot
  time.append(jogador.copy())
  while True:
    resp = str(input('Deseja continuar? [S/N]')).upper()[0]
    if resp in 'SN':
      break
    print('Você digitou uma informação errada.Digite novamente:')
  if resp == 'N':
    break
print('-=' * 30)
print(jogador)
print(time)
print('-=' * 30)
for k , v in enumerate(time):
  print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} fez {n} partidas')
for k, v in enumerate(jogador['gols']):
  print(f' ==> Na partida {k}, fez {v} gols')