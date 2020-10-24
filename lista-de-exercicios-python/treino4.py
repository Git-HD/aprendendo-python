#3. Implemente um programa que converta um peso expresso em pounds
#para kilograma (1 pound ~= 2.2 kilogramas). Como um peso não pode
#ser representado por um valor negativo, seu programa deve informar
#ao usuário que valores negativos são inválidos.
def libra_para_kg(libra):
    kg = libra / 2.2
    gramas = kg * 1000
    return int(kg), gramas % 1000

libra = float(input('Quantas libras? '))
kg, g = libra_para_kg(libra)
print('A quantidade de libras que você digitou é {}. Isto é {}kg e {}gramas.'.format(libra,kg,g))
