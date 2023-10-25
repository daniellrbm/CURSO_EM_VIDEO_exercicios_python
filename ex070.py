print('===== DESAFIO 70 =====')
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

totCompra = totMil = menor = cont = 0
barato = ''

while True:
    nomeProduto = str(input('Nome do Produto: ')).capitalize().strip()
    precoProduto = float(input('Preço: R$'))
    cont += 1
    # REGISTRANDO O PRODUTO DE MENOR PREÇO...
    if cont == 1 or precoProduto < menor:
        menor = precoProduto
        barato = nomeProduto

    # SOMANDO O TOTAL DA COMPRA...
    totCompra += precoProduto

    # REGISTRANDO OS PRODUTOS QUE CUSTAM MAIS DE MIL REAIS...
    if precoProduto > 1000:
        totMil += 1

    # CONTINUANDO O LOOP...
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N': # CONDIÇÃO DE PARADA...
        break

print('=' * 40)
print('DETALHAMENTO DA COMPRA:')
print(f'>> Total da compra: R${totCompra:.2f}')
print(f'>> {totMil} produtos custam mais de R$1.000')
print(f'>> O produto mais barato é {barato}, que custa R${menor}')