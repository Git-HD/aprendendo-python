from datetime import date
atual = date.today().year
nas = int(input('Ano de nascimento: '))
idade = atual - nas
if idade <= 9:
	print('Classificação: MIRIM')
elif idade >9 and idade <=14:
	print('Calissificação: INFANTIL')
elif idade > 14 and idade <=19:
	print('Classificação: JUNIOR')
elif idade >19 and idade <=25:
	print('Classificação: SÊNIOR')
elif idade >25:
	print('Classificação: Master')