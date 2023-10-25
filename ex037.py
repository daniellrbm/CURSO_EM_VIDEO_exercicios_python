print('===== DESAFIO 37 =====')
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))

opcao = int(input('='*20 +
                  '\nVocê escolheu o número {}\n'
                  'PARA QUAL BASE DESEJA CONVERTER?\n'
                  '[1] Binário;\n'
                  '[2] Octal;\n'
                  '[3] Hexadecimal;\n'
                  'SUA OPÇÃO: '.format(numero)))

if opcao == 1:
    print('\nO número {} em base binária é {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('\nO número {} em base octal é {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('\nO número {} em base hexadecinal é {}'.format(numero, hex(numero)))
else:
    print('\nOpção inválida. Tente Novamente.')