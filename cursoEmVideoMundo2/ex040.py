# media de notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media <= 5: print('Sua média foi : {} e você está reprovado'.format(media))
elif media > 5 or media <= 6.9: print('Sua média foi : {} e você está em recuperação'.format(media))
else: print('Sua média foi : {} e você está em recuperação'.format(media))
