# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de 
# gols feitos durante o campeonato.


jogador = dict()
partida = list()

jogador['nome'] = str(input('Nome do jogador: ')).title()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(0, tot):
    partida.append(int(input(f'Quantos gols fez na {c+1}ª partida?: ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'O elemento {k} tem o valor {v}')
print()
print(f'{jogador["nome"]} jogou {len(partida)} partidas:')
print()
for i, v in enumerate(jogador['gols']):
    print(f'=>  Na {i+1}ª partida fez {v} gols')
print()
print(f'Foi um total de {jogador["total"]} gols')