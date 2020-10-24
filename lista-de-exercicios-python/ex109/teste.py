import moeda

resp = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(resp)} é {moeda.metade(resp, True)}")
print(f"Aumentando {moeda.moeda(resp)} em 10% temos {moeda.aumentar(resp, 10, True)}")
print(f"O dobro de {moeda.moeda(resp)} é {moeda.dobro(resp, True)}")
print(f"Diminuindo {moeda.moeda(resp)} em 13% temos {moeda.diminuir(resp, 13, True)}")