print('===== DESAFIO 53 =====')
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()

#para eliminar espaços internos da frase
fraseArray = frase.split() #separa as palavras da frase num array
fraseJunta = ''.join(fraseArray) #reune os itens do array sem espaços numa palavra só

fraseInversa = fraseJunta[::-1] #tecnica de fatiamento para palavrasde trás pra frente, subistituindo o codigo em verde abaixo

'''fraseInversa = ''
for c in range(len(fraseJunta)-1, -1, -1):
    fraseInversa += fraseJunta[c]'''

#conferindo se a frase invertida é um palíndromo
if fraseJunta == fraseInversa:
    print('{} >>> {}.\n'
          'Temos um palíndromo! =)'.format(fraseJunta, fraseInversa))
else:
    print('{} >>> {}.\n'
          'Não temos um palíndromo. =('.format(fraseJunta, fraseInversa))