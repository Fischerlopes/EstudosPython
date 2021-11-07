# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

c = 0
lista_alunos = list()
lista_geral = list()
alunos = int(input(('Quantos alunos você quer digitar ? ')))
while c < alunos:
    nome = str(input('Digite o nome do aluno: '))
    lista_alunos.append(nome)
    nota1 = float(input('Digite a primeira nota: '))
    lista_alunos.append(nota1)
    nota2 = float(input('Digite a segunda nota: '))
    lista_alunos.append(nota2)
    média = (nota1 + nota2)/2
    lista_alunos.append(média)
    lista_geral.append(lista_alunos[:])
    lista_alunos.clear()
    c += 1
print('Segue relação dos Alunos cadastrados:')
for p, v in enumerate(lista_geral):
    print(f'{v[0]}')
print('Digite qual aluno você quer ver a média:')

for p, v in enumerate(lista_geral):
    print(f'{p} para {v[0]}')

n = int(input('Número: '))

print(f'A média do aluno {lista_geral[n][0]} é : {lista_geral[n][3]}')
print(f'A primeira nota do(a) aluno(a) {lista_geral[n][0]} é : {lista_geral[n][1]}')
print(f'A segunda nota do(a) Aluno(a) {lista_geral[n][0]} é: {lista_geral[n][2]}')

