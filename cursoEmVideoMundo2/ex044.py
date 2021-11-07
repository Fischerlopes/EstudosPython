print('===' * 6)

valorCompras = float(input("Total do pedido: R$ "))

print('''FORMA DE PAGAMENTO
[ 1 ] À VISTA
[ 2 ] A VISTA CARTÃO
[ 3 ] 2X CARTÃO
[ 4 ] 3X ou MAIS CARTÃO''')

parc = int(input('Qual a Opção ? '))

if parc == 1:
    print('O valor final das suas compras é R$: {}'.format(valorCompras - (valorCompras * 0.1)))
elif parc == 2:
    print('O valor final das suas compras é R$: {}'.format(valorCompras - (valorCompras * 0.05)))
elif parc == 3:
    print('O valor final das suas compras é R$: {}'.format(valorCompras))
elif parc == 4:
    totalparcelas = int(input('Qual o total de parcelas?'))
    valorfinal = valorCompras + valorCompras * 20 /100
    valorparcela = valorfinal / totalparcelas
    print('O valor final das suas compras é R$: {}, com uma parcela de '
          'R$ {}'.format(valorfinal, valorparcela))
else:
    print('Opção de pagamento inválida!!')