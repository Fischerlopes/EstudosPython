def aumentar(valor, taxa=10):
    valor += valor * (taxa/100)
    return valor


def diminuir(valor, taxa=10):
    valor -= valor * (taxa / 100)
    return valor


def dobro(valor):
    valor = valor * 2
    return valor


def metade(valor):
    valor = valor / 2
    return valor

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')