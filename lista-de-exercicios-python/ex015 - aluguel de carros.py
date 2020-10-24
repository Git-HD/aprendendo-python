dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preço = (dia*60) + (km*0.15)
print('O total a pagar é R${}'.format(preço))