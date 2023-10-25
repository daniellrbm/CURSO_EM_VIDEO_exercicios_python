# VERSÃO DO PRF GUANABARA DA RESOLUÇÃO DO DESAFIO 86

# GERANDO A MATRIZ: CADA LISTA INTERNA REPRESENTA UMA LINHA. CADA ITEM DENTRO DELAS É UMA COLUNA...
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# LOOPS ANINHADOS PRA PREENCHER LINHAS E COLUNAS COM OS VALORES DIGITADOS...
for lin in range(0, 3):
    for col in range (0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para ({lin}, {col}): '))

# LOOPS ANINHADOS PRA EXIBIR A MATRIZ CRIADA...
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^2}]', end='')
    print()
