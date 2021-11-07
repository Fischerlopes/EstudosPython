#Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(lar, alt):
  area = lar * alt
  print(f'Para as medidas {lar} e {alt}, a área é : {area} M² ')

area(2, 10)

for c in range(0,2):
  lar = float(input('Digite uma medida: '))
  alt = float(input('Digite uma altura: '))
  area(lar, alt)
