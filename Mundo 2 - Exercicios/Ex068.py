# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador
# PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Escolha um numero entre 0 a 10: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha PAR ou IMPAR? [P/I]: ')).strip().upper()[0]
        print(f'\033[36mO jogador jogou {jogador}, o computador {computador} o total é {total}',end='')
        print('\033[32m]- Deu PAR' if total % 2 == 0 else '\033[32m]- Deu IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('\033[32mParabéns, voce venceu!')
            v += 1
        else:
            print('\033[31mVocê perdeu, fim de jogo!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('\033[32mParabéns, você venceu!')
            v += 1
        else:
            print('\033[31mVocê perdeu, fim de jogo!')
            break
    print('\033[32mContinue jogando para conseguir mais pontos de vitória!')

if v > 4:
    print(f'\033[32mUau!, você conseguiu atingir um novo record de vitórias, PARABÉS! sua pontuação: {v}')
else:
    print(f'\033[36mSua pontuação de vitórias: {v}')
