def aumentar(n=0, taxa=0, formato=False):
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(n=0, taxa=0, formato=False):
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)

def metade(n, formato=False):
    res = n / 2
    return res if not formato else(moeda(res))

def dobro(n, formato=False):
    res = n * 2
    return res if not formato else(moeda(res))

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')

def resumo(n=0, taxa_aumento=0, taxa_reducao=0):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço: \t{dobro(n, True)}")
    print(f"Metade do preço: \t{metade(n, True)}")
    print(f"{taxa_aumento}% de aumento: \t{aumentar(n, taxa_aumento, True)}")
    print(f"{taxa_reducao}% de redução: \t{diminuir(n, taxa_reducao, True)}")
    print("-" * 30)

