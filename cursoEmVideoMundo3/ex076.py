palavras = ('rafael', 'maria', 'jose', 'sofia')

for c in palavras:
    print(f'\nNa palavra {c}, tem: ', end='')
    for pos in c:
        if pos in 'aeiou':
            print(f'{pos}', end='')





