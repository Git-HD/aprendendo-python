from random import randint
x = 'Sim'
objetos = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1,3)
print('=~=' *10)
print('GAME - PEDRA PAPEL E TESOURA')
print('=~=' *10)
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
print('=~=' *10)
player = int(input('Pedra papel ou tesoura? '))
print('=~=' *10)
print('O computador escolheu {}'.format(objetos[computador]))
print('Você escolheu {}'.format(objetos[player]))
print('=~=' *10)
if computador == 1:
    if player == 1:
        print('O jogo empatou!')
    elif player == 2:
        print('Você venceu!')
    elif player == 3:
        print('Você perdeu!')
    else:
        print('Erro - Somente números de 1 a 3')

elif computador == 2:
    if player == 1:
        print('Você perdeu!')
    elif player == 2:
        print('O jogo empatou!')
    elif player == 3:
        print('Você venceu!')
    else:
        print('Erro - Somente números de 1 a 3')

elif computador == 3:
    if player == 1:
        print('Você venceu!')
    elif player == 2:
        print('Você perdeu!')
    elif player == 3:
        print('O jogo empatou!')
    else:
        print('Erro - Somenete números de 1 a 3')










