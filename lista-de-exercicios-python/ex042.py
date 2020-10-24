seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if (seg2 - seg3) < seg1 < seg2 + seg3 and (seg1 - seg3) < seg2 < seg1 + seg3 and (seg1 - seg2) < seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM formar um Triângulo')
    if seg1 == seg2 == seg3:
        print('Triângulo EQUILÁTERO')
    if seg1 != seg2 != seg3 != seg1:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓCELES')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')