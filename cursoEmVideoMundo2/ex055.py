lista = []

for c in range(1, 6):
  peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
  lista.append(peso)

print(lista)
print('O maior dessa relação é {} Kg'.format(max(lista)))
print('O menor dessa relação é {} Kg'.format(min(lista)))