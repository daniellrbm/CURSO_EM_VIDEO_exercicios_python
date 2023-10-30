# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
print('===== DESAFIO 109 =====')

# Importando o múdulo
import moeda

# PROGRAMA PRINCIPAL
preco = float(input('DIGITE UM PREÇO: R$ '))
moeda.dobro(preco, True)
moeda.metade(preco, True)
moeda.aumentar(preco, True)
moeda.diminuir(preco, True)
