jogador = {}
partidas = []
lista_jogadores = []
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    total_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0, total_partidas):
        partidas.append(int(input(f"Quantos gols na partida {c}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista_jogadores.append(jogador.copy())
    cont = str(input("Quer continuar? [S/N] "))
    if cont in 'Nn':
        break
print('-=' * 30)
print("cod nome        gols          total")
print('-' * 30)
for j in range(0, len(lista_jogadores)):
    print(f"{j} {lista_jogadores[j]['nome']}         {lista_jogadores[j]['gols']}         {lista_jogadores[j]['total']}")
stop = 0
while stop != 999:
    res = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if res == 999:
        print("<< VOLTE SEMPRE >>")
        stop = 999
    elif res > len(lista_jogadores):
        print(f"Erro não existe jogador com o código {res}")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {lista_jogadores[res]['nome']}:")
        for j in range(0, len(lista_jogadores[res]['gols'])):
            print(f"No jogo {j + 1} fez {lista_jogadores[res]['gols'][j]}")
