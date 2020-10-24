def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))

# def ano_nasc():
#     from datetime import datetime
#     nasc = int(input("Em que ano você nasceu? "))
#     ano = datetime.now()
#     idade = ano.year - nasc
#     if idade > 25:
#         voto = str("VOTO OPCIONAL")
#     elif idade >= 18:
#         voto = str("VOTO OBRIGATÓRIO")
#     elif idade < 16:
#         voto = str("NÃO VOTA")
#     print(f"Com {idade} anos: {voto}")
# ano_nasc()