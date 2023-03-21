# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
itens = ['\033[32mPEDRA', '\033[32mPAPEL', '\033[32mTESOURA']
computador = randint(0, 2)
print('Olá, vamos jogar jokenpô, será que você consegue me vencer?')
jogador = int(input('O jogo começou! escolha a sua jogada (digite 0, 1 ou 2): '))

print('\033[34mJO')
sleep(1)
print('\033[34mKEN')
sleep(1)
print('\033[34mPÔOOO!')
print(f'\033[mO jogador jogou {itens[jogador]} \033[me o computador jogou {itens[computador]}')


if computador == 0:# ESCOLHEU PEDRA
    if jogador == 0:
        print('\033[36mEMPATE')
    elif jogador == 1:
        print('\033[36mJogador VENCE!')
    elif jogador == 2:
        print('\033[36mComputador VENCE!')
    else:
        print('\033[31mOpção invalida, tente novamente!')
elif computador == 1:# ESCOLHEU PAPEL
    if jogador == 0:
        print('\033[36mComputador VENCE!')
    elif jogador == 1:
        print('\033[36mEMPATE')
    elif jogador == 2:
        print('\033[36mJogador VENCE!')
    else:
        print('\033[31mOpção invalida, tente novamente!')
elif computador == 2:# ESCOLHEU TESOURA
    if jogador == 0:
        print('\033[36mJogador VENCE!')
    elif jogador == 1:
        print('\033[36mComputador VENCE!')
    elif jogador == 2:
        print('\033[36mEMPATE!')
    else:
        print('\033[31mOpção invalida, tente novamente!')
