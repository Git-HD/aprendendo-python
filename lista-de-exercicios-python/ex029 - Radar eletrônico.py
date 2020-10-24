vel = float(input('Qaul é a velocidade atual do carro? '))
if vel>80:
    print('MULTADO! Você excedeu o limite que é de 80Km/h')
    multa = (vel-80) * 7
    print('Você deve pagar uma multa de: R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')