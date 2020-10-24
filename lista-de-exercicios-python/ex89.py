list_aluno_notas = [[], [], [], []]
cont = 0
while True:
    nome = str(input("Nome: "))
    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    continuar = str(input("Quer continuar? [S/N] "))
    list_aluno_notas[0].append(nome)
    list_aluno_notas[1].append(n1)
    list_aluno_notas[2].append(n2)
    media = (n1 + n2) / 2
    list_aluno_notas[3].append(media)
    cont += 1
    if continuar in 'Nn':
        print('-=' * 30)
        print('NO. Nome Média')
        print('-' * 15)
        for aluno in range(0, cont):
            print(f"{aluno} {list_aluno_notas[0][aluno]} {list_aluno_notas[3][aluno]}")
        break
stop = 0
while stop == 0:
    nota_aluno = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if nota_aluno == 999:
        print('Finalizando...')
        print('<<< VOLTE SEMPRE >>>')
        stop = 999
    else:
        print('-' * 20)
        print(f"Notas de {list_aluno_notas[0][nota_aluno]} são [{list_aluno_notas[1][nota_aluno]}, {list_aluno_notas[2][nota_aluno]}]")
        print('-' * 20)

