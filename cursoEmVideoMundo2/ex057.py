#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo M/F: '))
while sexo not in 'FMmf':
    sexo = str(input('Dados inválidos, digite novamente :  ')).strip().lower()

print('Feminino' if sexo in 'Ff' else 'Masculino')
print(f' O valor digitado foi : {sexo}')


