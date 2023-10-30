# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
print('===== DESAFIO 108 =====')

# Importando o múdulo
import moeda

# PROGRAMA PRINCIPAL
preco = float(input('DIGITE UM PREÇO: R$ '))
moeda.dobro(preco)
moeda.metade(preco)
moeda.aumentar(preco)
moeda.diminuir(preco)
