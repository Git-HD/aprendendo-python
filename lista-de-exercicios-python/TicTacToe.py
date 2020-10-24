def jogar():
    print("TIC TAC TOE -- JOGO DA VELHA")
    print("-=" * 30)
    player_1 = str(input("Player 1 - Escolha entre X (x) ou Bola O (b): "))
    while player_1 not in 'XxBb':
        print("Somente X (x) ou Bola O (b) são permitidos.")
        player_1 = str(input("Escolha entre X (x) ou Bola O (b): "))
    if player_1 in 'Bb':
        player_1 = 'O'
        player_2 = 'X'
    else:
        player_1 = 'X'
        player_2 = 'O'
    print("   |   |      -->>>    (1,1) | (1,2) | (1,3) ")
    print("---|---|---   -->>>   -------|-------|-------")
    print("   |   |      -->>>    (2,1) | (2,2) | (2,3) ")
    print("---|---|---   -->>>   -------|-------|-------")
    print("   |   |      -->>>    (3,1) | (3,2) | (3,3) ")
    print("-=" * 30)
    count = 0

    quadro = {'1,1': ' ', '1,2': ' ', '1,3': ' ',
              '2,1': ' ', '2,2': ' ', '2,3': ' ',
              '3,1': ' ', '3,2': ' ', '3,3': ' '}

    quadro_chaves = []

    for key in quadro:
        quadro_chaves.append(key)

    def printQuadro(board):
        print(' ' + board['1,1'] + ' | ' + board['1,2'] + ' | ' + board['1,3'])
        print("---|---|---")
        print(' ' + board['2,1'] + ' | ' + board['2,2'] + ' | ' + board['2,3'])
        print("---|---|---")
        print(' ' + board['3,1'] + ' | ' + board['3,2'] + ' | ' + board['3,3'])

    for quadros in range(10):

        if count >= 5:
            if quadro['1,1'] == quadro['1,2'] == quadro['1,3'] != ' ':  # across the top
                printQuadro(quadro)
                print("\nFim de jogo.\n")
                print(" >>> Jogador " + quadro['1,3'] + " venceu. <<<")
                fim = str(input("Deseja jogar novamente? [S/N] "))
                if fim in 'Ss':
                    jogar()
                else:
                    print("\nAté a próxima")
                    break
            elif quadro['2,1'] == quadro['2,2'] == quadro['2,3'] != ' ':  # across the middle
                printQuadro(quadro)
                print("\nFim de Jogo.\n")
                print(" >>> Jogador " + quadro['2,3'] + " venceu. <<<")
                fim = str(input("Deseja jogar novamente? [S/N] "))
                if fim in 'Ss':
                    jogar()
                else:
                    print("\nAté a próxima")
                    break
            elif quadro['3,1'] == quadro['3,2'] == quadro['3,3'] != ' ':  # across the bottom
                printQuadro(quadro)
                print("\nFim de Jogo.\n")
                print(" >>> Jogador " + quadro['3,3'] + " venceu. <<<")
                fim = str(input("Deseja jogar novamente? [S/N] "))
                if fim in 'Ss':
                    jogar()
                else:
                    print("\nAté a próxima")
                    break
            elif quadro['3,1'] == quadro['2,1'] == quadro['1,1'] != ' ':  # down the left side
                printQuadro(quadro)
                print("\nFim de Jogo.\n")
                print(" >>> Jogador " + quadro['1,1'] + " venceu. <<<")
                fim = str(input("Deseja jogar novamente? [S/N] "))
                if fim in 'Ss':
                    jogar()
                else:
                    print("\nAté a próxima")
                    break
            elif quadro['3,2'] == quadro['2,2'] == quadro['1,2'] != ' ':  # down the middle
                printQuadro(quadro)
                print("\nFim de Jogo.\n")
                print(" >>> Jogador " + quadro['1,2'] + " venceu. <<<")
                fim = str(input("Deseja jogar novamente? [S/N] "))
                if fim in 'Ss':
                    jogar()
                else:
                    print("\nAté a próxima")
                    break
            elif quadro['3,3'] == quadro['2,3'] == quadro['1,3'] != ' ':  # down the right side
                printQuadro(quadro)
                print("\nFim de Jogo.\n")
                print(" >>> Jogador " + quadro['1,3'] + " venceu. <<<")
                fim = str(input("Deseja jogar novamente? [S/N] "))
                if fim in 'Ss':
                    jogar()
                else:
                    print("\nAté a próxima")
                    break
            elif quadro['1,1'] == quadro['2,2'] == quadro['3,3'] != ' ':  # diagonal
                printQuadro(quadro)
                print("\nFim de Jogo.\n")
                print(" >>> Jogador " + quadro['3,3'] + " venceu. <<<")
                fim = str(input("Deseja jogar novamente? [S/N] "))
                if fim in 'Ss':
                    jogar()
                else:
                    print("\nAté a próxima")
                    break
            elif quadro['3,1'] == quadro['2,2'] == quadro['1,3'] != ' ':  # diagonal
                printQuadro(quadro)
                print("\nFim de Jogo.\n")
                print(" >>> Jogador " + quadro['1,3'] + " venceu. <<<")
                fim = str(input("Deseja jogar novamente? [S/N] "))
                if fim in 'Ss':
                    jogar()
                else:
                    print("\nAté a próxima")
                    break

                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nFim de Jogo.\n")
            print("Empatou!!")
            fim = str(input("Deseja jogar novamente? [S/N] "))
            if fim in 'Ss':
                jogar()
            else:
                print("\nAté a próxima")
                break

        linha_1 = str(int(input(f"Player 1 ({player_1}) - Selecione uma linha (1 a 3): ")))
        coluna_1 = str(int(input(f"Player 1 ({player_1}) - Selecione uma coluna (1 a 3): ")))
        jogador1 = linha_1 + ',' + coluna_1
        if quadro[jogador1] == ' ':
            quadro[jogador1] = player_1
            count += 1
            printQuadro(quadro)
        else:
            while quadro[jogador1] != ' ':
                print(f"\nEsta posição já foi escolhida pelo jogador: >> {quadro[jogador1]} <<. Escolha novamente!\n")
                linha_1 = str(int(input(f"Player 1 ({player_1}) - Selecione uma linha (1 a 3): ")))
                coluna_1 = str(int(input(f"Player 1 ({player_1}) - Selecione uma coluna (1 a 3): ")))
                jogador1 = linha_1 + ',' + coluna_1
                count += 1
                printQuadro(quadro)

        linha_2 = str(int(input(f"Player 2 ({player_2}) - Selecione uma linha (1 a 3): ")))
        coluna_2 = str(int(input(f"Player 2 ({player_2}) - Selecione uma coluna (1 a 3): ")))
        jogador2 = linha_2 + ',' + coluna_2
        if quadro[jogador2] == ' ':
            quadro[jogador2] = player_2
            count += 1
            printQuadro(quadro)
        else:
            while quadro[jogador2] != ' ':
                print(f"\nEsta posição já foi escolhida pelo jogador: >> {quadro[jogador2]} <<. Escolha novamente!\n")
                linha_2 = str(int(input(f"Player 2 ({player_2}) - Selecione uma linha (1 a 3): ")))
                coluna_2 = str(int(input(f"Player 2 ({player_2}) - Selecione uma coluna (1 a 3): ")))
                jogador2 = linha_2 + ',' + coluna_2
                count += 1
                printQuadro(quadro)

jogar()
