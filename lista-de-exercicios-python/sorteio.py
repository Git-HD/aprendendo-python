from random import randint

def sortear():
    print("Sorteando 10 valores na lista: ", end='')
    lista_valores = []
    for valor in range(0, 10):
        lista_valores.append(randint(0, 10))
        print(lista_valores[valor], end=' ')
    return lista_valores

def somar_par(lista):
    par = 0
    for valor in range(0, 10):
        if lista[valor] % 2 == 0:
            par += lista[valor]
    print(f"\nSomando os valores pares de {lista}, temos {par}")


def somar_impar(lista):
    impar = 0
    for valor in range(0, 10):
        if lista[valor] % 2 == 1:
            impar += lista[valor]
    print(f"\nSomando os valores ímpares de {lista}, temos {impar}")

def maior(num):
    cont = maior = 0
    print("\nAnalisando os valores passados...")
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

def menor(num):
    cont = menor = 0
    print("\nAnalisando os vaores passados...")
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
            menor = valor
        else:
            if valor < menor:
                menor = valor
        cont += 1
    print(f'\nFrom informados {cont} valores ao todo.')
    print(f'O menor valor informado foi {menor}')

def media(num):
    soma = 0
    for valor in num:
        soma += valor
    media = soma / 10
    print(f'\nA média dos valores informados é {media}')


print(" ----- ANÁLISE DE SORTEIO DE NÚMEROS -----")
lista_global = sortear()
while True:
    print("\n 1 -- ANALISAR O MAIOR NÚMERO")
    print(" 2 -- ANALISAR O MENOR NÚMERO")
    print(" 3 -- SOMAR NÚMEROS PARES")
    print(" 4 -- SOMAR NÚMEROS ÍMPARES")
    print(" 5 -- MÉDIA DOS VALORES")
    print(" 6 -- ORDENAR SORTEIO DE FORMA CRESCENTE")
    print(" 7 -- ORDENAR SORTEIO DE FORMA DECRESCENTE")
    print(" 8 -- SORTEAR NOVAMENTE")
    resp = int(input("O que deseja fazer? "))
    if resp == 1:
        maior(lista_global)
        fim = str(input("Acessar o menu? [S/N] "))
        if fim in 'Ss':
            continue
        else:
            print("\nAté a próxima")
            break
    elif resp == 2:
        menor(lista_global)
        fim = str(input("Acessar o menu? [S/N] "))
        if fim in 'Ss':
            continue
        else:
            print("\nAté a próxima")
            break
    elif resp == 3:
        somar_par(lista_global)
        fim = str(input("Acessar o menu? [S/N] "))
        if fim in 'Ss':
            continue
        else:
            print("\nAté a próxima")
            break
    elif resp == 4:
        somar_impar(lista_global)
        fim = str(input("Acessar o menu? [S/N] "))
        if fim in 'Ss':
            continue
        else:
            print("\nAté a próxima")
            break
    elif resp == 5:
        media(lista_global)
        fim = str(input("Acessar o menu? [S/N] "))
        if fim in 'Ss':
            continue
        else:
            print("\nAté a próxima")
            break
    elif resp == 6:
        lista_global.sort()
        print(lista_global)
        fim = str(input("Acessar o menu? [S/N] "))
        if fim in 'Ss':
            continue
        else:
            print("\nAté a próxima")
            break
    elif resp == 7:
        lista_global.sort(reverse=True)
        print(lista_global)
        fim = str(input("Acessar o menu? [S/N] "))
        if fim in 'Ss':
            continue
        else:
            print("\nAté a próxima")
            break
    elif resp == 8:
        lista_global = sortear()


