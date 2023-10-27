#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
print('===== desafio 104 =====')

def leiaInt(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            int(num)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return num



# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')