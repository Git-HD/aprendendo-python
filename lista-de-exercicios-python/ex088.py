from random import randint
list = []
jogos =[]
quant = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in list:
            list.append(num)
            cont += 1
        if cont >= 6:
            break
    list.sort()
    jogos.append(list[:])
    list.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")