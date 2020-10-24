#3. Implemente um programa que converta um peso expresso em pounds
#para kilograma (1 pound ~= 2.2 kilogramas). Como um peso não pode
#ser representado por um valor negativo, seu programa deve informar
#ao usuário que valores negativos são inválidos.

def poundsToMetric(pounds):
    kilograms = pounds / 2.2
    grams = kilograms * 1000
    return int(kilograms), grams % 1000

pounds = float(input("How many Pounds? "))
kg, g = poundsToMetric(pounds)
print('The amount of pounds you entered is {}. '\
      'This is {} kilograms and {} grams.'.format(pounds, kg, g))