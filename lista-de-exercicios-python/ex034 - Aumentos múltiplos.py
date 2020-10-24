salario = float(input('Qual é o salário do funcionário? R$'))
#Aumento pode ser salario * 1.1 ou salario + (salario * 10/100)
if salario >= 1250.00:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15
print('Quem ganhava R${:.2f} agora passa a ganhar R${:.2f}!'.format(salario, aumento))