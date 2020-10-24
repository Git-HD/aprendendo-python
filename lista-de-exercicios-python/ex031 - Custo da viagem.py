dist = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar sua viagem de {:.2f}Km.'.format(dist))
if dist <= 200:
    preço = dist * 0.5
else:
    preço = dist * 0.45
print('E o preço da sua passagem sera de R${:.2f}.'.format(preço))