def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: um ou mais notas dos alunos (aceita várias).
        :param show: (opcional) Indicando se deve ou não adicionar a situação.
        :return: dicionário com várias informações da turma.
    """
    dados = {}
    soma = cont = maior = menor = 0
    dados['total'] = len(n)
    for valor in n:
        soma += valor
        media = (soma / len(n))
        dados['media'] = media
        if cont == 0:
            maior = valor
            menor = valor
        else:
            if valor > maior:
                maior = valor
            elif valor < menor:
                menor = valor
        cont += 1
    if sit:
        if dados['media'] >= 3 and dados['media'] <= 5:
            dados['situação'] = 'RUIM'
        elif dados['media'] >= 5 and dados['media'] <= 7:
            dados['situação'] = 'MÉDIA'
        else:
            dados['situação'] = 'BOA'
    dados['maior'] = maior
    dados['menor'] = menor
    print(dados)



resp = notas(10, 10, 10, 5, 4, sit=True)
print(resp)
help(notas)