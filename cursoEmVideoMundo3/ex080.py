#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

list = []

#uso do for por que sabemos a quantidade de itens que serão add.
for c in range(0,5):
    n = int(input('Digite um número: '))
# condição para verificar se o número digitado é o primeiro da lista ou o último
    if c == 0 or n > list[-1]:
        list.append(n)
        print('Adicional ao final da lista ...')
    else:
        pos = 0
        #while para percorrer todos os itens da lista
        while pos < len(list):
          #condição para verificar se o item digitado n é menor que o valor da posição da lista
            if n <= list[pos]:
            #se sim, adicionar o valor na lista
                list.insert(pos, n)
                break
            pos =+ 1
print(list)