#digitar vários valores, colocar numa lista e dividir em duas outras listas (ímpares e pares)

lista = []
lista_par = []
lista_impar = []

while True:
    s = str(input('Quer digitar um valor ? [S/N]: ')).strip()[0]
    if s in 'Nn':
        break
    n = int(input('Digite um  valor: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(lista)
print(lista_par)
print(lista_impar)