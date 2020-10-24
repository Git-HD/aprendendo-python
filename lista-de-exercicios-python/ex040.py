n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, med))
if 7 > med >= 5:
    print('RECUPERAÇÃO')
elif med < 5:
    print('REPROVADO')
else:
    print('APROVADO')