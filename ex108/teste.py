from ex108 import moeda

#for c in range(3):
  #  print(moeda.aumentar(c, 10))
   # print(moeda.diminuir(c, 10))
   # print(moeda.dobro(c))
   # print(moeda.metade(c))

valor = float(input('Digite um valor R$ : '))
print(f'{moeda.moeda(valor)} {moeda.moeda(moeda.aumentar(valor))}')
print(f'{moeda.moeda(valor)} {moeda.moeda(moeda.diminuir(valor))}')
print(f'{moeda.moeda(valor)} {moeda.moeda(moeda.dobro(valor))}')
print(f'{moeda.moeda(valor)} {moeda.moeda(moeda.metade(valor))}')