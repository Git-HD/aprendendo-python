from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    op = int(input('Qual sua opção? '))
    if op == 1:
        s = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, s))
    elif op == 2:
        prod = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, prod))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif op ==4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa!')