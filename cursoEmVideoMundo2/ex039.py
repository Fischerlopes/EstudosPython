# alistamento militar - condicionais aninhados
from datetime import date

anonasc = int(input('Digite seu ano de nascimento : '))
genero = str(input('Qual seu gênero: Masculino ou Feminino: M ou F ')).lower()

today = date.today()
difyear = today.year - anonasc
if genero == 'f':
    print('No Brasil, para você, o alistamento não é obrigatório')
else:
    print('Quem nasceu em {}, tem {} anos'.format(anonasc, difyear))
    if difyear == 17:
        print('Você deve se alistar imadiatamente')
    elif difyear > 17:
        print('Você perdeu o prazo de alistamente em {} anos'.format(difyear - 17))
    else:
        print('Ainda faltam {} anos para você se alistar'.format(17 - difyear))
