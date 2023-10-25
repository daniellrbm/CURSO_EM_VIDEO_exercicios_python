print('===== DESAFIO 80 =====')
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

listaNum = []

for cnt in range(0, 5):
    num = int(input('Digite um valor: '))
    # SE O CONTADOR FOR IGUAL A ZERO OU MAIOR QUE O ÚLTIMO ELEMENTO...
    if cnt == 0 or num > listaNum[-1]:
        listaNum.append(num)
        print('Valor adicionado ao fim da lista...')
        print('-' * 50)
    else: # CASO CONTRÁRIO...
        pos = 0
        while pos < len(listaNum):
            if num <= listaNum[pos]:
                listaNum.insert(pos, num)
                print(f'Valor foi adicionado na posição {pos} da lista...')
                print('-' * 50)
                break
            pos += 1
print('=' * 50)
print(f'A lista criada foi {listaNum}')
