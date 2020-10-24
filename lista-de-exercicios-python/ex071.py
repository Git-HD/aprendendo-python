print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)
v = int(input('Qual valor você quer sacar? R$'))
t = v
ced = 50
tced = 0
while True:
    if t >= ced:
        t -= ced
        tced += 1
    else:
        if tced > 0:
            print(f'Total de {tced} células de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tced = 0
        if t == 0:
            break
print('=' *30)
print('Volte sempre ao BANCO CEV! Bom dia!')
