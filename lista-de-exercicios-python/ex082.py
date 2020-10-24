list = []
while True:
    valor = str(input("Digite um valor: "))
    list.append(valor)
    continuar = str(input("Deseja continuar? [S/N] "))
    if continuar in 'Nn':
        break
print(f"A lista completa é {list}")
lista_pares = []
lista_impares = []
for valor in range(0, len(list)):
    numero_da_lista = int(list[valor])
    if numero_da_lista % 2 == 0:
        lista_pares.append(numero_da_lista)
    else:
        lista_impares.append(numero_da_lista)
print(f"A lista de pares é {lista_pares}")
print(f"A lista de ímpares é {lista_impares}")