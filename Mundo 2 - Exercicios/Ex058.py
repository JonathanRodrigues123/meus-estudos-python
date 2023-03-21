# Melhore o jogo do DESAFIO 028 onde o computador vai ''pensar'' em um numero entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Olá, sou seu amigo virtual, vamos jogar um game?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Escolha sua jogada entre 0 a 10: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    if jogador > computador:
        print('Menos... tente mais uma vez!')
    if jogador < computador:
        print('Mais... tente mais uma vez!')
if palpite == 1:
    print('Parabéns, você acertou de primeira!')
else:
    print(f'Fim de jogo com {palpite} tentativas, precisa treinar mais! ')
        

