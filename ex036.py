print('===== DESAFIO 36 =====')
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Perguntando o valor da casa
valor = float(input('Qual o valor do imóvel que deseja comprar? RS'))

# Perguntanto  a renda do comprador
salario = float(input('Qual o seu salário atual? R$'))

# Perguntando o tempo de financiamento
tFinan = int(input('Em quanto tempo deseja financiar o imóvel? '))

# Calculando valor da parcela
parcela = (valor/tFinan) / 12

if parcela <= (salario * 0.3):
    print('Valor do Imóvel: R${:.2f}.\n'
          'Tempo de Financiamento: {} anos\n'
          'Valor das Parcelas: R${:.2f}\n'
          'Sua renda É COMPATÍVEL com este financiamento.\n'
          'EMPRÉSTIMO AUTORIZADO.'.format(valor, tFinan, parcela))
else:
    print('Valor do Imóvel: R${:.2f}.\n'
          'Tempo de Financiamento: {} anos\n'
          'Valor das Parcelas: R${:.2f}\n'
          'Sua renda NÃO É COMPATÍVEL com este financiamento.\n'
          'EMPRÉSTIMO NÃO AUTORIZADO.'.format(valor, tFinan, parcela))