# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro
# de futebol, na ordem de colocação.Depois mostre:

#A) Apenas os 5 primeiros colocados.
#B) Os ultimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da chapecoense.


times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR',
'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino',
'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude', 'chapecoense')

print('TABELA DO CAMPEONATO DO BRASILEIRÃO')

print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print(f'A chapecoense encontra-se na {times.index("chapecoense")}ª posição')
print(f'A ordem da tabela em alfabética:')
print('-'*32)
for t in sorted(times):
    print(t)