# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

geral = list()
pessoas = dict()
lista_mulheres = ()
lista_velhos = ()
sum = media = 0
n = int(input('Quantas pessoas você quer cadastar ? '))
for c in range(0,n):
  pessoas['nome'] = str(input('Nome:'))
  pessoas['sexo'] = str(input('Sexo:'))
  pessoas['idade'] = int(input('idade:'))
  sum += pessoas['idade']
  geral.append(pessoas.copy())
print(geral)
print(f'O total de pessoas cadastradas foi {n}')
media = sum/n
print(f'A média de idade das pessoas é {media}')
for p in geral:
  if p['sexo'] in 'Ff':
    print(f'A lista das pessoas com sexo F são: {p["nome"]}')
for i in geral:
  if i['idade'] > media:
    print(f'As pessoas que estão acima da média de idade são: {i["nome"]}')
