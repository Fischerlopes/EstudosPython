num1 = int(input('Digite o primeiro número : '))
num2 = int(input('Digite o segundo número : '))
user_choice = 0

while user_choice != 5:
    print('Menu')
    user_choice = int(input('Digite a opção desejada : '))
    if user_choice == 1:
        print(f'Você escolheu a opção soma e o resultado é :{num1 + num2}')
    elif user_choice == 2:
        print(f'Você escolheu a opção multiplicar e o resultado é :{num1 * num2}')
    elif user_choice == 3:
        if num1 > num2:
            print(f'Você escolheu a opção maior e o maior valor é o : {num1}')
        else:
            print(f'Você escolheu a opção maior e o maior valor é o : {num2}')
    elif user_choice == 4:
        print(f'Você escolheu a opção Novos Números, então ')
        num1 = int(input('Digite o primeiro número : '))
        num2 = int(input('Digite o segundo número : '))

    elif user_choice > 5:
        print('voce digitou uma opção inválida! escolha novamente')


if user_choice == 5:
        print('Você digitou uma opção Fim do Programa, então ate mais!!')


