list = []

maior = 0
menor = 0

for n in range(0, 5):
    list.append(int(input(f'Digite um valor para posição {n}:')))
    if n == 0:
        maior = menor = list[n]
    else:
        if list[n] > maior:
            maior = list[n]
        if list[n] < menor:
            menor = list[n]

print(f"O maior valor digitado foi {maior} nas posições ", end='')
for i, v in enumerate(list):
    if v == maior:
        print(f'{i}... ', end='')
print(f"O menor valor digitado foi {menor} nas posições ", end='')
for i, v in enumerate(list):
    if v == menor:
        print(f'{i}... ', end='')
