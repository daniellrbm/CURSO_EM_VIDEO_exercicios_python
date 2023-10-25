print('===== DESAFIO 72 =====')
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tNum = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO',
        'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
        'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE',
        'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    #SE O NÚMERO ESTIVER ENTRE 0 E 20...
    if 0 <= num <= 20:
        print('=' * 40)
        print(f'Você digitou o número {tNum[num]}.')

        # OPÇÃO DE CONTINUAR OU NÃO...
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('=' * 40)
        while opcao not in 'SN':
            opcao = str(input('\033[1;31mOPÇÃO INVÁLIDA:\033[m Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao == 'N':
            break

    # SE O NÚMERO NÃO ESTIVER ENTRE 0 E 20...
    else:
        print('\033[1;33mTENTE NOVAMENTE.\033[m', end=' ')
print('FIM DO PROGRAMA.')