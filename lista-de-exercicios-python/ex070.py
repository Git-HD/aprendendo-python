print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
t = tmil = cont = 0
barato = ''
while True:
    p = str(input('Nome do produtor: '))
    pr = float(input('Preço: R$'))
    t += pr
    if pr > 1000:
        tmil += 1
    if cont == 1 or pr < menor:
        menor = pr
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:^40}'.format('Fim do programa!'))
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {tmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

