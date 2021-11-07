#calculo de IMC

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / ( altura**2)
if imc <= 18.5:
    print('Seu IMC é: {:.2f} e você está abaixo do peso!!'.format(imc))
elif imc <= 25:
    print('Seu IMC é de : {:.2f} e você está no Peso Ideal!!'.format(imc))
elif imc <= 30:
    print('Seu IMC é de: {:.2f} e você está  com Sobre Peso!!'.format(imc))
elif imc <= 40:
    print('Seu IMC é de : {:.2f} e você está Obseso!!'.format(imc))
else:
    print('Seu IMC é de : {:.2f} e você está com Obesidade Mórbida'.format(imc))
