# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
print('===== DESAFIO 110 =====')

# Importando o múdulo
import moeda

# PROGRAMA PRINCIPAL
preco = float(input('DIGITE UM PREÇO: R$ '))
# parâmentros pedidos: preco, taxa e desconto
moeda.resumo(preco, 10, 10)
