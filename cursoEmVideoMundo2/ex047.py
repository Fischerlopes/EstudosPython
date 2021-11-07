# motrar todos os pares de 1 a 50
list = []
for c in range(2, 51):
    if c % 2 == 0:
        list.append(c)
print(list)

list1 = []
for c in range(2, 51, 2):
    list1.append(c)
print(list1)
