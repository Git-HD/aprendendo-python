x = int(input('Pimeiro valor: '))
y = int(input('Segundo valor: '))
z = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
# Verificando quem é maior
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
