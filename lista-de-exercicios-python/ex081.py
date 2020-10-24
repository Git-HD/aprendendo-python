
list = []
while True:
    valor = str(input("Digite um valor: "))

    list.append(valor)

    continuar = str(input("Deseja continuar? [S/N] "))
    if continuar in 'Nn':
        break

list.reverse()
print(f"Você digitou {len(list)} elementos")
print(f"Você digitou os valores {list}")
if '5' in list:
    print("Valor 5 encontrado na lista")
else:
    print("Valor 5 não foi encontrado na lista")