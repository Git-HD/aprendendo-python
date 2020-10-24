soma = 0
contador = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        contador += 1
        soma = soma + x
print('A soma do total de {} valores é {}'.format(contador, soma))