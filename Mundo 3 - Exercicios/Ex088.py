# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
quant = int(input('Quantos jogos você quer sortear?: '))
tot = 1
print('MEGA SENA 2023'.center(30))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'\033[32mSORTEANDO {quant} JOGOS'.center(30))
for i, l in enumerate(jogos):
    print(f'\033[37mJogo{i+1}: {l}')
    sleep(1)
print('\033[32mBOA SORTE!'.center(30))

        