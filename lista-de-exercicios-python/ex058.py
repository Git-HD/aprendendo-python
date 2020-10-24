from random import randint

rand = randint(0, 10)
print("""Sou seu computador...\nAcabei de pensar em um número de 0 a 10.\nSerá que você consegue advinhar qual foi?""")
acertou = False
tentativas = 0
while not acertou:
    pal = int(input('Qual seu palpite? '))
    tentativas += 1
    if rand == pal:
        acertou = True
    else:
      if rand < pal:
        print('''Menos... Tente mais uma vez.''')
      elif rand > pal:
        print('''Menos... Tente mais uma vez.''')
print('Acertou com {} tentativas. Parabéns'.format(tentativas))

