# Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.]


from random import randint
from time import sleep
from operator import itemgetter
jogo = {
        'Jogador 1'.center(5): randint(1, 6),
        'Jogador 2'.center(5): randint(1, 6),
        'Jogador 3'.center(5): randint(1, 6),
        'Jogador 4'.center(5): randint(1, 6)
}
ranking = list()
print('JOGO DA SORTE:'.center(30))
for k, v in jogo.items():
    print(f'{k} jogou {v} no dado')
    sleep(2)
ranking = sorted(jogo.items(), key=itemgetter(0), reverse=True)
for i, v in enumerate(ranking):
    print(f'Em {i+1}ª Lugar foi {v[0]} jogou {v[1]} no dado')
    sleep(2)
print('CONGRATULAÇÃO!'.center(40))