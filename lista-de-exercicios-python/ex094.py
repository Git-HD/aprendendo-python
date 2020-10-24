pessoa = {}
lista_pessoa = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    pessoa['sexo'] = str(input("Sexo: [M/F] "))
    while pessoa['sexo'] not in 'MmFf':
        print("ERRO! Por favor, digite apenas M ou F")
        pessoa['sexo'] = str(input("Sexo: [M/F] "))
        continue
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    lista_pessoa.append(pessoa.copy())
    resp = str(input("Quer continuar? [S/N]? "))
    if resp in 'Nn':
        break
    while resp not in 'Ss':
        print("ERRO! Responda apenas S ou N.")
        resp = str(input("Quer continuar? [S/N]? "))
print('-=' * 30)
print(f"A) Ao todo temos {len(lista_pessoa)} pessoas cadastradas.")
media = soma / len(lista_pessoa)
print(f"B) A média de idade é de {media:5.2f} anos.")
print("C) As mulheres cadastradas foram", end='')
for p in lista_pessoa:
    if p['sexo'] in 'Ff':
        print(f" {p['nome']} ", end='')
print()
print("D) Lista das pessoas que estão acima da média: ", end='')
for p in lista_pessoa:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f" {k} = {v}; ", end='')
print("<< Encerrado >>")
