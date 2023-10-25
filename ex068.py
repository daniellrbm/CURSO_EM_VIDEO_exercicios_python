print('===== DESAFIO 68 =====')
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('PAR OU ÍMPAR???')
print('=' * 40)
rodadas = 0

while True:
    cpu = randint(1, 10)
    num = int(input('Digite um valor: '))
    opcao = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()
    soma = num + cpu
    print('=' * 40)

    # DEFININDO A SOMA DOS NÚMEROS COLOCADOS PELO JOGADOR E PC...
    if soma % 2 == 0:
        pOUi = 'PAR'
    else:
        pOUi = 'Ímpar'

    # DEFININDO O RESULTADO DO JOGO...
    if opcao == 'P' and pOUi == 'PAR':  # VITÓRIA PAR...
        print(str(f'\033[1mVocê jogou {num}. O PC jogou {cpu}.\n'
                  f'O total destes números é {soma}. Deu {pOUi}.\033[m\n'
                  f'\033[1;32mVOCÊ GANHOU!\033[m'))
        print('=' * 40)
    elif opcao == 'I' and pOUi == 'ÍMPAR':  # VITÓRIA ÍMPAR...
        print(str(f'\033[1mVocê jogou {num}. O PC jogou {cpu}.\n'
                  f'O total destes números é {soma}. Deu {pOUi}.\033[m\n'
                  f'\033[1;32mVOCÊ GANHOU!\033[m'))
        print('=' * 40)
    else:  # DERROTA...
        print(str(f'\033[1mVocê jogou {num}. O PC jogou {cpu}.\n'
                  f'O total destes números é {soma}. Deu {pOUi}.\033[m\n'
                  f'\033[1;31mVOCÊ PERDEU!\033[m'))
        break  # SE O JOGADOR PERDER, O PROGRAMA SERÁ ENCERRADO...

    rodadas += 1  # CONTABILIZANDO AS RODADAS EM CASO DE VITÓRIA...

print('=' * 40)
print(f'FIM DE JOGO!\n'
      f'Você havia vencido {rodadas} seguidas.')