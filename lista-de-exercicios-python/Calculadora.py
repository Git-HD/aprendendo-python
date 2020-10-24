from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('CALCULADORA')

def sair():
    print('Calculadora encerrada')
    exit()


def soma():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    resultado_mais = (n1 + n2)
    return ('A soma de {:.0f} e {:.0f} é: {:.2f}!'.format(n1, n2, resultado_mais))


def subtraçao():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    resultado_menos = (n1 - n2)
    return ('A subtração de {:.0f} e {:.0f} é: {:.2f}!'.format(n1, n2, resultado_menos))


def divisao():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    resultado_divisao = (n1 / n2)
    return ('A divisão de {:.0f} e {:.0f} é: {:.2f}!'.format(n1, n2, resultado_divisao))


def multiplicaçao():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    resultado_multiplicaçao = (n1 * n2)
    return ('A multiplicação de {:.0f} e {:.0f} é: {:.2f}!'.format(n1, n2, resultado_multiplicaçao))


def exp():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    resultado_exp = (n1 ** n2)
    return ('A exponenciação de {:.0f} elevado a {:.0f} é: {:.2f}!'.format(n1, n2, resultado_exp))


calculadora = {0: sair, 1: soma, 2: subtraçao, 3: divisao, 4: multiplicaçao, 5: exp}
cal = -1
while cal != 0:
    cal = int(input('CALCULADORA DE ADIÇÃO,SUBTRAÇÃO,DIVISÃO, MULTIPLICAÇÃO E EXPONENCIAÇÃO\n' +
                    'Somar - 1\n' +
                    'Subtrair - 2\n' +
                    'Dividir - 3\n' +
                    'Multiplicar - 4\n' +
                    'Elevar - 5\n' +
                    'Sair - 0 : '))
    print(calculadora[cal]())
root.mainloop()