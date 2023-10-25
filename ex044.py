print('===== DESAFIO 44 =====')
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

preco = float(input('Qual o valor da sua compra? R$'))
pgto = int(input('Qual a condição de pagamento?\n'
                 '[1] A vista dinheiro/Pix: 10% de desconto;\n'
                 '[2] A vista débito: 5% de desconto;\n'
                 '[3] Parcelado 2x: sem juros;\n'
                 '[4] Parcelado 3x ou mais: + 20% de juros\n'
                 'SUA OPÇÃO: '))

if pgto == 1:
    print('\nVocê terá um desconto de 10%.\n'
          'Sua compra sairá por R${:.2f}.'.format(preco * 0.9))
elif pgto ==2:
    print('\nVocê terá um desconto de 5%.\n'
          'Sua compra sairá por R${:.2f}.'.format(preco * 0.95))
elif pgto == 3:
    print('\nParcelamento em 2x sem acréscimos.\n'
          'Cada parcela sairá por R${:.2f}.'.format(preco / 2))
elif pgto == 4:
    preco2 = preco * 1.2
    parc = int(input('Quantas parcelas? '))
    if parc < 3:
        print('Valor inválido. O mínimo são 3 parcelas')
    else:
        print('\nParcelamento em 3x ou mais: Acréscimo de 20% de juros.\n'
              'O total da compra será de R${:.2f}.\n'
              'Dividido em {}x de R${:.2f}.'.format(preco2, parc, preco2/parc))
else:
    print('\nOpção Inválida. Tente Novamente')


