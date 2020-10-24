from random import randint
v = 0
while True:
    print('=-' * 30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 30)
    n = int(input('Digite um valor: '))
    c = randint(0, 11)
    tot = (n + c)
    tipo = ' '
    while tipo not in 'PI':
       tipo = str(input('Par ou ímpar? ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {c}. Total de {tot} ', end='')
    print('Deu Par' if tot % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes.')
