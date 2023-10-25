print('===== DESAFIO 61 =====')
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

ptermo = int(input('Primeiro termo da PA: '))
razao = int(input('Progressão da PA: '))
c = 1
addTermos = 10
totTermos = 0

print('=-' * 20)
print('OS PRIMEIROS 10 TERMOS DESTA PA SÃO:')
while addTermos != 0:
    totTermos += addTermos # VALOR DE TOTTERMOS SERÁ ATUALIZADO SEMPRE QUE DIGITARMOS UM NOVO VALOR NA PERGUNTA, EXCETO ZERO.

    # LACO PARA GERAR OS 10 PRIMEIROS TERMOS DA PA E AS ADIÇÕES DIGITADAS
    while c <= totTermos:
        print(ptermo, end=' >> ') # IMPRIME O PRIMEIRO TERMO ATUAL
        ptermo += razao # SOMA-SE A RAZÃO AO VALOR DO PRIMEIRO TERMO ATUAL
        c += 1 # ADICIONA UM NÚMERO AO VALOR INICIAL DO CONTADOR
    print('PAUSA...')
    print('=-' * 20)
    addTermos = int(input('Quantos termos mais desta PA deseja ver? '))

# SE O VALOR DIGITADO FOR ZERO, SAÍMOS DO LAÇO...
print('=-' * 20)
print('PA encerrada após exibir {} termos.'.format(totTermos))
print('FIM')








