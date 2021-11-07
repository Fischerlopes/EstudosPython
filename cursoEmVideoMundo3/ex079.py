#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


num =[] # criei uma lista vazia que receberá todos os valores
entrada = 0 # Criar uma variável para receber os valores para adicionar na lista
while True: # criar um laço infito para verificar n números
    choice = str(input('Você quer adicionar um número ? [S / N]: ')).strip()[0]
    # criar condição de saída do laço
    if choice in 'Nn':
        break
    else:
        #criar condição de validção se o número já está na lista ou não
        entrada = int(input('Digite um número: '))
        if entrada in num:
            print('Número já consta na lista! Não será adicionado!')
        else:
            num.append(entrada)
            print(f'O número {entrada}, foi adicionado com sucesso!!')
#imprimir os valores da lista ordenados
print(f'Os valores digitados foram: {sorted(num)}')

