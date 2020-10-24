
def aumentar(n):
    return n * 1.10

def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


