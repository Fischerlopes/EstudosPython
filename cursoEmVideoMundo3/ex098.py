# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada

from time import sleep
def contador(x, y, z):
  for c in range(x, y + 1, z):
   print(c, end=' ')
   sleep(0.5)
   print()
  for a in range(0, 11, 1):
    print(a, end=' ')
    sleep(0.5)
    print()
  for b in range(10, 0 , -2):
    print(b, end=' ')
    sleep(0.5)

print('-=' *30)


contador(0, 20, 2)