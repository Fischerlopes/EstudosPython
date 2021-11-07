def aumentar(valor, taxa=10, formato=False):
    res = valor + (valor * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(valor, taxa=10, formato=False):
    res = valor - (valor * taxa/100)
    return res if formato is False else moeda(res)


def dobro(valor, formato=False):
    res = valor * 2
    return res if not formato else moeda(res)


def metade(valor, formato=False):
    res = valor / 2
    return res if not formato else moeda(res)

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')