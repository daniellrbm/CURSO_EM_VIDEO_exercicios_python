print("===== DESAFIO 94 =====")
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

galera = list()
pessoa = dict()
soma = media = 0

while True:
    #limpando o dicionario pessoa...
    pessoa.clear()
    # Incluindo chaves e valores dentro do dicionário...
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['genero'] = str(input('Gênero [M/F]: ')).upper()[0]
        # exigindo que o genero seja M ou F...
        if pessoa['genero'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    # Gerando uma cópia do dicionário criado dentro da lista galera
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('PESSOA CADASTRADA. Continuar? [S/N]: ')).upper()[0]
        # exigindo que a resposta seja S ou N...
        if resposta in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    # encerrando o programa se a resposta for N...
    if resposta == 'N':
        break
# Exibindo os resultados
print("=-" * 20)
## A. Quantas pessoas foram cadastradas...
print(f'>> Foram cadastradas {len(galera)} pessoas;')
## B. A média de idade das pessoas cadastradas...
media = soma / len(galera)
print(f'>> A média de idade destas pessoas é {media:.2f} anos;')
## C. Mulheres Cadastradas...
print('>> As mulheres cadastradas foram:')
for pessoa in galera:
    if pessoa['genero'] in 'Ff':
        print(f'    ** {pessoa["nome"]};')
## D. Pessoas acima com idade acima da média...
print(f'>> As pessoas com idade acima da média são:')
for pessoa in galera:
    if pessoa['idade'] > media:
        print(f'    ** {pessoa["nome"]} ({pessoa["idade"]} anos);')
