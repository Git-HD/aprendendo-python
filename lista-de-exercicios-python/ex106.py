from time import sleep

c = ('\033[m',       # 0 - sem cores
     '\033[0;30;41m',  #1 - vermelho
     '\033[0;30;42m',  #1 - verde
     '\033[0;30;43m',  #1 - amarelo
     '\033[0;30;44m',  #1 - azul
     '\033[0;30;45m',  #1 - roxo
     '\033[7;30m',  #1 - branco
     '');

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)