#custo de uma viagem
valor = int(input(('Digite a distância da viagem em Km: ')))
print('O valor da viagem é : R$ {}'.format(valor * 0.5) if valor <= 200 else('O valor da viagem é R$ {}'.format(valor * 0.45)))
