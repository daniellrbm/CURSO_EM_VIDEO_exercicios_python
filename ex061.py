print('===== DESAFIO 61 =====')
# efaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# CÓDIGO EXERCÍCIO 51
'''ptermo = int(input('Primeiro termo da PA: '))
razao = int(input('Progressão da PA: '))
dtermo = ptermo + (10 - 1) * razao

for c in range(ptermo, dtermo + razao, razao):
    print(c, end=' >> ')
print('Fim da PA')'''

ptermo = int(input('Primeiro termo da PA: '))
razao = int(input('Progressão da PA: '))
c = 1

print('=-' * 20)
print('OS PRIMEIROS 10 TERMOS DESTA PA SÃO:')
while c <= 10:
    print(ptermo, end=' >> ') # IMPRIME O PRIMEIRO TERMO
    ptermo += razao # SOMA-SE A RAZÃO AO VALOR DO PRIMEIRO TERMO
    c += 1 # ADICIONA UM NÚMERO AO VALOR INICIAL DO CONTADOR
print('FIM DA PA')



