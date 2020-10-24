
num = list()
while True:
    valor = str(input("Digite um valor: "))
    if valor not in num:
        num.append(valor)
        print("Valor adicionado com sucesso")
    else:
        print("Valor duplicado! ")
    continuar = str(input("Deseja continuar? [S/N] "))
    if continuar in 'Nn':
        break

num.sort()
print(f"Você digitou os valores {num}")