from random import randint

print('===== DESAFIO 45 =====')
# Crie um programa que faça o computador jogar Jokenpô com você.

# DETERMINANDO A ESCOLHA DO JOGADOR
player = int(input('\nJOKENPÔ ==> ESCOLHA SUA JOGADA:\n'
                   '[1] PEDRA\n'
                   '[2] PAPEL\n'
                   '[3] TESOURA\n'
                   'SUA JOGADA: '))

if player == 1:
    print('\nVocê escolheu PEDRA')
elif player == 2:
    print('\nVocê escolheu PAPEL')
else:
    print('\nVocê escolheu TESOURA')

# DETERMINANDO A ESCOLHA DO PC
pc = randint(1,3)

if pc == 1:
    print('O PC escolheu PEDRA')
elif pc == 2:
    print('O PC escolheu PAPEL')
else:
    print('O PC escolheu TESOURA')

# DETERMINANDO O RESULTADO DO JOGO
if player == 1: #Se o jogador escolher PEDRA
    if pc == 1: #pedra x pedra
        print('Empate. Tente novamente.')
    elif pc == 2: #pedra x papel
        print('Voce perdeu. Tente Novamente')
    elif pc == 3: #pedra x tesoura
        print('Você ganhou. Parabéns!')

elif player == 2: # Se o jogador escolher PAPEL
    if pc == 1: #papel x pedra
        print('Voce ganhou. Parabéns!')
    elif pc == 2: #papel x papel
        print('Empate. Tente novamente.')
    elif pc == 3: #papel x tesoura
        print('Você perdeu. Tente novamente.')

elif player ==3: #Se o jogador escolher TESOURA
    if pc == 1: #tesoura x pedra
        print('Você perdeu. Tente novamente.')
    elif pc == 2: #tesoura x papel
        print('Voce ganhou. Parabéns!')
    elif pc == 3: #tesoura x tesoura
        print('Empate. Tente novamente.')