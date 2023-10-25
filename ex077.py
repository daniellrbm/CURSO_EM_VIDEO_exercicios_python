print('===== DESAFIO 77 =====')
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('daniel', 'do', 'rio', 'branco', 'matheus')
print(palavras)

# PARA CADA ITEM DA TUPLA (PARA SEPARAR AS PALAVRAS)...
for item in palavras:
    print(f'\nA palavra {item.upper()} tem as vogais ', end='')
    # PARA CADA LETRA DE CADA ITEM DA TUPLA (PARA SEPARAR AS VOGAIS DE CADA PALAVRA)...
    for letra in item:
        if letra in 'aeiou':
            print(f'{letra.upper()} ', end='')

