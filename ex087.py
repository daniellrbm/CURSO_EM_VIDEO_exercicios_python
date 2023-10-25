print('===== DESAFIO 87 =====')
# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

# GERANDO A MATRIZ: CADA LISTA INTERNA REPRESENTA UMA LINHA. CADA ITEM DENTRO DELAS É UMA COLUNA...
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = totcol3 = mailin2 = 0

# LOOPS ANINHADOS PRA PREENCHER LINHAS E COLUNAS COM OS VALORES DIGITADOS...
for lin in range(0, 3):
    for col in range (0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para ({lin}, {col}): '))
        # FAZENDO A SOMA DE TODOS OS VALORES PARES DIGITADOS...
        if matriz[lin][col] % 2 == 0:
            totpar += matriz[lin][col]

        # FAZENDO A SOMA DOS ITENS DA 3a COLUNA
        if matriz[lin][2]:
            totcol3 += matriz[lin][2]

        # IDENTIFICANDO O MAIOR VALOR DA 2a LINHA...
        if matriz[1][col] > mailin2:
            mailin2 = matriz[1][col]
print('=' * 40)
print('>> A MATRIZ CRIADA FOI:')
# LOOPS ANINHADOS PRA EXIBIR A MATRIZ CRIADA...
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^3}]', end='')
    print()

print(f'>> A soma dos valores pares digitados é {totpar}.')
print(f'>> A some dos itens da 3a coluna é {totcol3}.')
print(f'>> O maior valor da 2a linha é {mailin2}.')