print('===== DESAFIO 86 =====')
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], [], [], [], [], [], [], []]
qtd = 0

for lin in range(0, 3):
    for col in range(0, 3):
        matriz[qtd] = int(input(f'Digite um valor para ({lin}, {col}): '))
        qtd += 1
print('=' * 40)
print('A matriz criada foi:')
print(f'[{matriz[0]}] [{matriz[1]}] [{matriz[2]}]'
      f'\n[{matriz[3]}] [{matriz[4]}] [{matriz[5]}]'
      f'\n[{matriz[6]}] [{matriz[7]}] [{matriz[8]}]')

