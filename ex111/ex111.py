# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
print('===== DESAFIO 111 =====')

# Importando o múdulo
from utilidadecev import moeda

# PROGRAMA PRINCIPAL
preco = float(input('DIGITE UM PREÇO: R$ '))
# parâmentros pedidos: preco, taxa e desconto
moeda.resumo(preco, 10, 10)
