

maioridade = 0
nomevelho = ''
totalmulher = 0
idade = []
for c in range(1, 5):
  nomes = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip()
  idades = int(input('Digite a idade da {}ª pessoa: '.format(c)))
  idade.append(idades)
  sexos = str(input('Digite o sexo da {}ª pessoa: (M / F) '.format(c))).strip().lower()
  if c == 1 and sexos in 'm':
    maioridade = idades
    nomevelho = nomes
  if sexos in 'm'and idades > maioridade:
    maioridade = idades
    nomevelho = nomes
  if sexos in 'f' and idades < 20:
    totalmulher =+ 1


print('A média de idade das pessoas é:{} '.format(sum(idade) / len(idade)))
print('O nome do homem mais velho é: {} e tem {} anos'.format(nomevelho, maioridade))
print('Ao todo tem {} mulheres com idade menor que 20 anos'.format(totalmulher))