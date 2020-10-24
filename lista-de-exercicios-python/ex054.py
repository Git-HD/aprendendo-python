from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for x in range(1, 8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(x)))
    idade = atual - ano
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))