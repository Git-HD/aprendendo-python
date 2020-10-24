somaidade = 0
medidade = 0
maioridadehomem = 0
nomevelho = ''
for x in range(1, 5):
    print('----- {}ª pessoa -----'.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if x == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

medidade = somaidade / 4
print('A média de idade do grupo é {} anos'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))

