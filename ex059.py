print('===== DESAFIO 59 =====')
# Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números, [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
opcao = 0

while opcao != 5:
    # APRESENTANDO O MENU DO PROGRAMA...
    print('=-' * 20)
    print('Você escolheu os números {} e {}.\n'
          'O que deseja fazer?\n'
          '[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] APONTAR O MAIOR NÚMERO\n'
          '[4] ESCOLHER NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAMA'.format(n1, n2))
    print('=-' * 20)
    opcao = int(input('>>> Sua opção: ')) # ESCOLHEDO SUA OPÇÃO
    print('=-' * 20)

    if opcao == 1: # OPÇÃO SOMAR
        soma = n1 + n2
        print('\033[33mVOCÊ ESCOLHEU SOMAR:\n'
              '{} + {} = {}\033[m'.format(n1, n2, soma))

    elif opcao == 2: # OPÇÃO MULTIPLICAR
        produto = n1 * n2
        print('\033[33mVOCÊ ESCOLHEU MULTIPLICAR:\n'
              '{} X {} = {}\033[m'.format(n1, n2, produto))

    elif opcao == 3: # OPÇÃO MAIOR NÚMERO
        if n1 > n2:
            print('\033[33mVOCÊ ESCOLHEU APOSTAR O MAIOR NÚMERO:\n'
                  '{} É MAIOR QUE {}\033[m'.format(n1, n2))
        elif n2 > n1:
            print('\033[33mVOCÊ ESCOLHEU APOSTAR O MAIOR NÚMERO:\n'
                  '{} É MAIOR QUE {}\033[m'.format(n2, n1))
        else:
            print('\033[33mVOCÊ ESCOLHEU APOSTAR O MAIOR NÚMERO:\n'
                  'OS VALORES ESCOLHIDOS SÃO IGUAIS\033[m')

    elif opcao == 4:
        print('\033[33mVOCÊ OPTOU POR ESCOLHER NOVOS NÚMEROS:\033[m')
        n1 = int(input('\033[33mDigite um novo 1º número: \033[m'))
        n2 = int(input('\033[33mDigite um novo 2º número: \033[m'))

    elif opcao > 5:
        print('\033[31mOpção inválida. Tente novamente.\033[m')

# ESCOLHENDO A OPÇÃO 5...
print('\033[33mEncerrando o programa. Até a próxima!\033[m')