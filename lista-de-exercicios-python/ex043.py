peso = float(input('Qual seu peso? (Kg) '))
alt = float(input('Qual sua altura? (M) '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('ABAIXO do peso')
elif 18.5 <= imc < 25:
    print('Peso IDEAL')
elif 25 <= imc < 30:
    print('Peso SOBREPESO')
elif 30 <= imc < 40:
    print('Peso OBESIDADE')
elif imc >= 40:
    print('Obesidade Mórbida')
