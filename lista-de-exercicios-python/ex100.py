from random import randint

def sortear():
    print("Sorteando 5 valores na lista: ", end='')
    lista_valores = []
    for valor in range(0, 5):
        lista_valores.append(randint(0, 10))
        print(lista_valores[valor], end=' ')
    return lista_valores


def somar(lista):
    par = 0
    for valor in range(0, 5):
        if lista[valor] % 2 == 0:
            par += lista[valor]
    print(f"\nSomando os valores pares de {lista}, temos {par}")
somar(sortear())