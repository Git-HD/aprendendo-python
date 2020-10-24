def sair():
    print('Calculadora encerrada')
    exit()


def soma():
    n1 = float(input('Digite o primeiro n�mero: '))
    n2 = float(input('Digite o segundo n�mero: '))
    resultado_mais = (n1 + n2)
    return ('A soma de {:.0f} e {:.0f} �: {:.2f}!'.format(n1, n2, resultado_mais))


def subtracao():
    n1 = float(input('Digite o primeiro n�mero: '))
    n2 = float(input('Digite o segundo n�mero: '))
    resultado_menos = (n1 - n2)
    return ('A subtra��o de {:.0f} e {:.0f} �: {:.2f}!'.format(n1, n2, resultado_menos))


def divisao():
    n1 = float(input('Digite o primeiro n�mero: '))
    n2 = float(input('Digite o segundo n�mero: '))
    resultado_divisao = (n1 / n2)
    return ('A divis�o de {:.0f} e {:.0f} �: {:.2f}!'.format(n1, n2, resultado_divisao))


def multiplicacao():
    n1 = float(input('Digite o primeiro n�mero: '))
    n2 = float(input('Digite o segundo n�mero: '))
    resultado_multiplicacao = (n1 * n2)
    return ('A multiplica��o de {:.0f} e {:.0f} �: {:.2f}!'.format(n1, n2, resultado_multiplicacao))


def exp():
    n1 = float(input('Digite o primeiro n�mero: '))
    n2 = float(input('Digite o segundo n�mero: '))
    resultado_exp = (n1 ** n2)
    return ('A exponencia��o de {:.0f} elevado a {:.0f} �: {:.2f}!'.format(n1, n2, resultado_exp))


calculadora = {0: sair, 1: soma, 2: subtracao, 3: divisao, 4: multiplicacao, 5: exp}
cal = -1
while cal != 0:
    cal = int(input('CALCULADORA DE ADI��O,SUBTRA��O,DIVIS�O, MULTIPLICA��O E EXPONENCIA��O\n' +
                    'Somar - 1\n' +
                    'Subtrair - 2\n' +
                    'Dividir - 3\n' +
                    'Multiplicar - 4\n' +
                    'Elevar - 5\n' +
                    'Sair - 0 : '))
    print(calculadora[cal]())