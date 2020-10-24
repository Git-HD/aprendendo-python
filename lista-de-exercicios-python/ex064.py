n = cont = soma = 0
n = int(input('Digite o número [999 paraparar]: '))
while n != 999:
    n = int(input('Digite o número [999 paraparar]: '))
    soma += n
    cont += 1
print('Você digitou {} números. E a soma entre eles foi {}'.format(cont, soma))