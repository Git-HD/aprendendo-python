from random import randint
ops = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual é a sua jogada? '))
print('Computador jogou {}'.format(ops[pc]))
print('Jogador jogou {}'.format(ops[jog]))
if pc == 0:
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('JOGADOR VENCEU!')
    elif jog == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida')
elif pc == 1:
    if jog == 0:
        print('COMPUTADOR VENCEU!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('JOGADOR VENCEU!')
    else:
        print('Jogada inválida')

elif pc == 2:
    if jog == 0:
        print('JOGADOR VENCEU!')
    elif jog == 1:
        print('COMPUTADOR VENCEU!')
    elif jog == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida')




