largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
tinta = area/2
print('Sua parede tem dimensão de {}x{}, sua área é de {}m² e precisará de {:.0f}L de tinta.'.format(largura, altura, area, tinta))