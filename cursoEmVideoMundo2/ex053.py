nome = str(input('Digite a frase que você quer analisar:  ')).strip().lower()
palavras = nome.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('teste de palavras:{} {}'.format(junto, inverso))
if junto == inverso:
  print('A frase digita é um palíndromo, pois {} é igual a {} de trás para frente'.format(nome, junto))
else:
  print('A frase digitada não é um palíndromo')
