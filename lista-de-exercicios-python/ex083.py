exp = str(input("Digite a expressão: "))
pilha = []

for parenteses in pilha:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        pilha.append(')')
    if len(pilha) > 0:
        pilha.pop()
if len(pilha) == 0:
    print("Sua expressão é válida")
else:
    print("Expressão inválida")