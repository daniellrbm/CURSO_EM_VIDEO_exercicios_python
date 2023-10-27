# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: A) Quantidade de notas B) A maior nota C) A menor nota D) A média da turma E) situação (opcional)
print('===== DESAFIO 105 =====')

def notas(*n, sit=False):
    '''
    Função para analisar notas e a situação de aluno(s):
    :param n: uma ou mais notas de um estudante;
    :param sit: Valor opcional. Caso True, exibirá a situação do estudante com base em suas notas e média;
    :return: dicionário contendo informações variadas do estudante.
    '''
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n) / len(n)
    if sit:
        if dic['media'] < 4:
            dic['situação'] = 'Muito Ruim'
        elif dic['media'] < 6:
            dic['situação'] = 'Ruim'
        elif dic['media'] < 8:
            dic['situação'] = 'Boa'
        elif dic['media'] < 9:
            dic['situação'] = 'Muito Boa'
        else:
            dic['situação'] = 'Excelente'
    return dic


# PROGRAMA PRINCIPAL
resp = notas(10, 9, 9, sit=True)
print(resp)
help(notas)