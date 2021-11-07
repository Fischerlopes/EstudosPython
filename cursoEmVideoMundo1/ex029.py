a = int(input('Digite a velocidade do carro : '))
print('Velocidade permitida, boa viagem!!' if a <= 30 \
          else 'Você está acima da velocidade permitida, sua multa é :  R$ {}'.format((a - 60) * 3,5))