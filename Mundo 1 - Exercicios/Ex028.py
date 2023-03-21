# Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o numero escolhido pelo computador.O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print('Olá, sou o computador e acabei de pensar um um numero entre 0 e 5!')
print('Será que você consegue adivinhar em qual numero eu pensei?')
jogador = int(input('Escolha sua jogada: '))
print('-='*30)
print('Analizando o resultado...')
sleep(1)
print(f'O jogador jogou {jogador} e o computador jogou {computador}')
print('-='*30)
if jogador == computador:
    print('Você acertou,tem uma otima percepção, parabéns!?')
else:
    print('O computador venceu,fim de jogo !')