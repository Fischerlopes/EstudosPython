#comparador de números

firstNumber = int(input('Digite o primero número: '))
secondNumber = int(input('Digite o segundo número: '))

if firstNumber > secondNumber:
    print('O primeiro número é o maior')
elif secondNumber > firstNumber:
    print('O segundo número é o maior')
else:
    print('Os números são iguais')

