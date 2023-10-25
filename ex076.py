print('===== DESAFIO 76 =====')
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.5,
            'Caderno', 9.99,
            'Borracha', 3.75,
            'Estojo', 15.9,
            'Caneta', 5,
            'Mochila', 69.99)

# PARA CADA POSIÇÃO ENTRE ZERO E A EXTENÇÃO DA TUPLA...
for pos in range(0, len(produtos)):
    # SE A POSIÇÃO FOR PAR...
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    # SE A POSIÇÃO FOR ÍMPAR...
    else:
        print(f'R${produtos[pos]:>6.2f}')