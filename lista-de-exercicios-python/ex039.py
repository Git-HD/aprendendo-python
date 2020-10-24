from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar!')
elif idade <18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade >18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos'.format(saldo))








#ano = int(input('Ano de nascimento: '))
#nascimento = 2018 - ano
#print('Quem nasceu em {} tem {} anos em 2018'.format(ano, nascimento))
#if nascimento >= 18:
    #print('Você deve se alistar')
#else:
    #print('Você tem que se alistar daqui a {} anos'.format(1)