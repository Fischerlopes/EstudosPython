frase = 'Curso em Video Python'
print(frase[0::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.replace('Python', 'Rafael e Joao'))
print(frase)
print(frase.upper())
## print(frase.upper('Python')) - não aceita apenas uma palavra
print(frase.capitalize())
print(frase.title())
frase1 = '   testando uma string  '
print(frase1)
print(len(frase1))
a = frase1.strip()
print(len(a))
frase2 = '   testando uma string  '
b = frase2.lstrip()
print(len(b))
frase3 = '   testando uma string  '
c = frase3.rstrip()
print(len(c))

print(frase1.split())
