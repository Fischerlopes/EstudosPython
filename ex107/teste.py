import moeda

#for c in range(3):
  #  print(moeda.aumentar(c, 10))
   # print(moeda.diminuir(c, 10))
   # print(moeda.dobro(c))
   # print(moeda.metade(c))

valor = float(input('Digite um valor R$ : '))
print(moeda.aumentar(valor))
print(moeda.diminuir(valor))
print(moeda.dobro(valor))
print(moeda.metade(valor))