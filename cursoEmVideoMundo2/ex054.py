from datetime import date

list = []
list1 = []
atual = date.today().year
count = 0
count1 = 0

for c in range(1, 8):
  datas = int(input('Digite o ano de nascimento da {}ª pessoa (AAAA): '.format(c)))
  if ( atual - datas ) >= 60:
    list.append(datas)
    count =+ 1
  else:
     list1.append(datas)
     count1 += 1

print('Essas pessoas: {} atingiram a terceira idade!'.format(list))
print('Essa(s) pessoa(s): {} não atingiu/atingiram a terceira idade!'.format(list1))
