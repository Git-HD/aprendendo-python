import datetime
year = datetime.datetime.now()
trabalhador = {}
trabalhador['nome'] = str(input("Nome: "))
trabalhador['nascimento'] = int(input("Ano de nascimento: "))
trabalhador['idade'] = int(year.year) - trabalhador['nascimento']
trabalhador['ctps'] = int(input("Carteira de trabalho (0 não tem): "))
if trabalhador['ctps'] == 0:
    print("-=" * 30)
    print(f" - nome tem o valor {trabalhador['nome']}")
    print(f" - idade tem o valor {trabalhador['idade']}")
    print(f" - ctps tem o valor {trabalhador['ctps']}")
else:
    trabalhador['contratacao'] = int(input("Ano de contratação: "))
    trabalhador['salario'] = int(input("Salário: "))
    trabalhador['aposentadoria'] = (trabalhador['contratacao'] - trabalhador['nascimento']) + 35
    print("-=" * 30)
    print(f" - nome tem o valor {trabalhador['nome']}")
    print(f" - idade tem o valor {trabalhador['idade']}")
    print(f" - ctps tem o valor {trabalhador['ctps']}")
    print(f" - contratação tem o valor de {trabalhador['contratacao']}")
    print(f" - salário tem o valor de {trabalhador['salario']}")
    print(f" - aposentadoria tem o valor de {trabalhador['aposentadoria']}")

# solucao video
# dados = {}
# dados['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de Nascimento: '))
# dados['idade'] = datetime.now().year - nasc
# if dados['ctps'] != 0:
#     dados['contratacao'] = int(input('Ano de Contratação: '))
#     dados['salario'] = float(input('Salário: R$'))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
# print('-=' * 30)
# for k, v in dados.items():
#     print(f' - {k} tem o valor {v}')