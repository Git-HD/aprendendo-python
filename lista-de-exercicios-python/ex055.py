maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(x)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))