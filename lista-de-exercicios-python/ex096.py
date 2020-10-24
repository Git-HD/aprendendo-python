# print("Controle de Terrenos")
# print("-" * 30)
# larg = float(input("Largura (m): "))
# comp = float(input("Comprimento (m): "))
# def result():
#     resultado = larg * comp
#     print(f"A área de um terreno {larg}x{comp} é de {resultado}m²")
# result()

def área(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg}x{comp} é de {a}m².")

print(" Controle de Terrenos")
print('-' * 20)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
área(l, c)