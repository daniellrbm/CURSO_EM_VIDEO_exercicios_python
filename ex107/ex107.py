# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
print('===== DESAFIO 107 =====')

# Importando o múdulo
import moeda

# PROGRAMA PRINCIPAL
preco = float(input('DIGITE UM PREÇO: R$ '))
moeda.dobro(preco)
moeda.metade(preco)
moeda.aumentar(preco)
moeda.diminuir(preco)
