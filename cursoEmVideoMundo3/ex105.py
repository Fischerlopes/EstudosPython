#  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
#  um dicionário com as seguintes informações:
#– Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)

def notas(* núm):
  relação_notas = {}
  lista = []
  soma = 0
  c = 0
  resp = ''
  while resp in 'Ss':
    relação_notas[c] = float(input(f'Digite a nota na posição {c}: '))
    resp = str(input('Deseja lançar mais alguma nota? '))
    lista = relação_notas.copy()
    soma += relação_notas[c]
    c +=1
    if resp in 'Nn':
      break
  print(f'As notas digitadas foram : {lista}')
  print(f'A maior nota foi: {max(lista)}')
  print(f'A menor nota foi: {min(lista)}')
  print(f'A quantidade de notas lancadas foi: {len(lista)}')
  print(f' A média é: {soma/len(lista)}')

notas()