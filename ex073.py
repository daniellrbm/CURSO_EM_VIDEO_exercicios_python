print('===== DESAFIO 73 =====')
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

bras23 = ('BOT', 'FLA', 'PAL', 'GRE', 'FLU', 'CAP', 'BRG',
          'SPFC', 'CUI', 'CRU', 'FOR', 'COR', 'CAM', 'INT',
          'GOI', 'SAN', 'BAH', 'CTB', 'AMG', 'VAS')

print('=' * 40)
print(f'O G4 do Brasileirão 2023 após 17 rodadas é comporto por {bras23[0:4]}')
print('=' * 40)
print(f'O Z4 do Brasileirão 2023 após 17 rodadas é comporto por {bras23[-4:]}')
print('=' * 40)
print(f'O código dos times em ordem alfabética é {sorted(bras23)}')
print('=' * 40)
print(f'O time do Cuiabá está na {bras23.index("CUI")+1}ª posição.')