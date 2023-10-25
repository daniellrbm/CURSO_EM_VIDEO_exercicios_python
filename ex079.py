print('===== DESAFIO 79 =====')
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
listaNum = []

while True:
        num = int(input('Digite um valor: '))
        # SE O VALOR DE NUM NÃO CONSTAR NA LISTA...
        if num not in listaNum:
            listaNum.append(num)
            print('\033[32mVALOR ADICIONADO À LISTA!\033[m', end=' ')
        # CASO JÁ CONSTE...
        else:
            print('\033[33mESTE VALOR JÁ CONSTA NA LISTA.\nDIGITE OUTRO.\033[m', end=' ')

        opcao = str(input('Deseja continuar? S/N ')).strip().upper()[0]
        print('-' * 50)
        while opcao not in 'SN':
            opcao = str(input(f'\033[31mOPÇÃO INVÁLIDA.\033[m Deseja continuar? S/N ')).strip().upper()[0]
            print('-' * 50)
        if opcao == 'N':
            print('=' * 50)
            break

# EXIBINDO A LISTA CRIADA EM ORDEM CRESCENTE....
print(f'A lista criada em ordem crescente é {sorted(listaNum)}')