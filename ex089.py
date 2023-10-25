print('===== DESAFIO 89 =====')
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

listaGeral = []

while True:
    # GERANDO OS INPUTS NECESSÁRIOS...
    nome = str(input('NOME DO ALUNO: ')).strip().capitalize()
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    med = (n1 + n2) / 2
    # ADICIONANDO OS INPUTS NUMA SUBLISTA DENTRO DA LISTA PRINCIPAL...
    listaGeral.append([nome, [n1, n2], med])
    resp = str(input('>> Cadastrar novo aluno? [S/N] '))
    if resp in 'Nn':
        break
    print('=' * 40)
print('=' * 40)

# IMPRIMINDO A LISTA COM OS DADOS DOS ALUNOS
print(f'{"#":<3}{"NOME DO ALUNO":<15}{"MÉDIA":<5}')
print('-' * 40)
for i, alu in enumerate(listaGeral):
    # IMPRIMINDO NUMERO, NOME E MEDIA
    print(f'{i:<3}{alu[0]:<15}{alu[2]:<5.1f}')

# ACESSANDO AS NOTAS DE DETERMINADO ALUNO...
print('=' * 40)
while True:
    num = int(input('Deseja ver as notas de qual aluno (#)? (999 para encerrar) '))
    if num <= len(listaGeral):
        # IMPRIMINDO O NOME DO ALUNO E SUAS RESPECTIVAS NOTAS
        print(f'>> As notas de {listaGeral[num][0].upper()} foram {listaGeral[num][1]}')
        print('=' * 40)
    if num == 999:
        print('ENCERRANDO O PROGRAMA...')
        break