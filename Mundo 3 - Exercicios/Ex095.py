# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um
# sistema de visualização de detalhes do aproveitamento de cada jogador.

from time import sleep
jogador = dict()
partida = list()
time = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f'Quantos gols fez na {c+1}ª partida?: ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO: Por favor digite apenas S ou N!')
    if resp == 'N':
        break
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:>15} ', end='')
print()
print('-'*60)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):>15} ', end='')
    print()
    print('-'*60)
while True:
    busca = int(input('Quer Mostrar dados de qual jogador? (digite 999 para encerrar!): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe nenhum jogador com o código: {busca}')
    else:
        print('-'*40)
        print(f'Dados do jogador {time[busca]["nome"]}')
        print('-'*40)
        for i, g in enumerate(time[busca]['gols']):
            print('-'*40)
            print(f'Na {i+1}ª partida fez {g} gols')
            print('-'*40)
print('Finalizando aguarde...')            
sleep(3)
print('-'*30)
print('Programa finalizado!')
print('-'*30)