import moeda

resp = float(input("Digite o preço: R$"))
print(f"A metade de {resp} é {moeda.metade(resp)}")
print(f"Aumentando {resp} em 10% temos {moeda.aumentar(resp)}")
print(f"O dobro de {resp} é {moeda.dobro(resp)}")