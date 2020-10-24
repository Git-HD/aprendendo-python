print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
t18 = th = tm = 0
while True:
    i = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F]')).strip().upper()[0]
    if i >= 18:
        t18 += 1
    if sex == 'M':
        th += 1
    if sex == 'F' and i < 20:
        tm += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {t18}')
print(f'Ao todo temos {th} homens cadastrados')
print(f'E temos {tm} mulheres com menores de 20 anos')

