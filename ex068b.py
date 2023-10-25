# VERSÃO DA CORREÇÃO DO PROFESSOR GUANABARA

from random import randint

vit = 0

while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    total = computador + jogador
    pOUi = ' '
    while pOUi not in 'PI':
        pOUi = str(input('Sua aposta: PAR ou ÍMPAR??? [P/I]: ')).upper().strip()[0]

    print('=' * 40)
    print(f'Você jogou {jogador}. O PC jogou {computador}. O total é {total}.')

    if pOUi == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU! Vamos jogar novamente...')
            print('=' * 40)
            vit += 1
        else:
            print('VOCÊ PERDEU.')
            break
    if pOUi == 'I':
        if total % 2 != 0:
            print('VOCÊ VENCEU! Vamos jogar novamente...')
            print('=' * 40)
            vit += 1
        else:
            print('VOCÊ PERDEU.')
            break
print('=' * 40)
print(f'GAME OVER. Você ganhou {vit} rodada.')