#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
func = dict()
func = { 'Nome': str(input('Digite o nome do colaborador: ')),
          'Ano de Nascimento': int(input('Ano de Nascimento: ')),
          'Carteira de trabalho:' : int(input('Digite o número da carteira de trabalho: '))}
if func['Carteira de trabalho:'] != 0:
  func['Ano de Contratação'] = int(input('Ano de Contratação: '))
  func['Salário'] = float(input('Salário: '))
  func['Idade: '] = date.today().year - func['Ano de Nascimento']
  func['Aposentadoria: '] = func['Ano de Contratação'] + 35 - func['Ano de Nascimento']
print(func)