print('{:=^40}'.format('LOJAS AMERICANAS'))
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTEO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    total = p - (p * 10 / 100)
elif op == 2:
    total = p - (p * 5 / 100)
elif op ==3:
    total = p
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif op ==4:
    total = p + (p * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua comra de {:.2f}R$ vai custar {:.2f}R$ no final'.format(p, total))