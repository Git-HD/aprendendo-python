# matriz = []
# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         resp = matriz.append(int(input(f"Digite um valor para [{linha}, {coluna}]: ")))
#
# print(matriz)
# print()
# print(f"[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]")
# print(f"[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]")
# print(f"[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]")

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()