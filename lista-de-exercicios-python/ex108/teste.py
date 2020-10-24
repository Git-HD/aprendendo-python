import moeda

resp = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(resp)} é {moeda.moeda(moeda.metade(resp))}")
print(f"Aumentando {moeda.moeda(resp)} em 10% temos {moeda.moeda(moeda.aumentar(resp))}")
print(f"O dobro de {moeda.moeda(resp)} é {moeda.moeda(moeda.dobro(resp))}")