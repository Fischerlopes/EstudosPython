
valorCasa = float(input('Digite o valor da Casa: '))
salaryBuyer = float(input('Digite seu salário : '))
pagamentoEmAnos = int(input('Digite em quantos anos você pretende pagar a casa : '))

valorPrestacao = valorCasa / (pagamentoEmAnos * 12)

print('Para o salário de: R$ {}, o valor da prestação não excede os 30%, então --> Empréstimo aprovado'.format(salaryBuyer) if valorPrestacao <= (0.3 * salaryBuyer) else 'Empréstimo negado')

