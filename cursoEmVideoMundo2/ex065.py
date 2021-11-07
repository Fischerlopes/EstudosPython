#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

list = []
sum = count = 0
teste = ''
while True:
    n = int(input('Digite um valor : '))
    sum = sum + n
    count += 1
    list.append(n)
    teste = input('Você deseja continuar  [Y/N] ? ').strip().lower()
    media = sum / len(list)
    if teste != 'y':
        break
print(f'Você digitou {count} valores, a média é : {media}')
print(f'o maior valor é : {max(list)}, e o menor valor é : {min(list)}')


