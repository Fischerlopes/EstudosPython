tupla = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
for c in tupla:
    c = int(input('Digite um número de 0 a 20: '))
    if c <= 20:
        print(f'o número que você escolheu foi {c} e seu valor por extenso é: {tupla[c - 1]}')
        break
    else:
        print('Você digitou um número inválido')

