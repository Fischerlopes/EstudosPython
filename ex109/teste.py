from ex109 import moeda

#for c in range(3):
  #  print(moeda.aumentar(c, 10))
   # print(moeda.diminuir(c, 10))
   # print(moeda.dobro(c))
   # print(moeda.metade(c))

valor = float(input('Digite um valor R$ : '))
print(f'{moeda.moeda(valor)} {moeda.aumentar(valor,10, True)}')
print(f'{moeda.moeda(valor)} {moeda.diminuir(valor, 10,  True)}')
print(f'{moeda.moeda(valor)} {moeda.dobro(valor, True)}')
print(f'{moeda.moeda(valor)} {moeda.metade(valor, True)}')