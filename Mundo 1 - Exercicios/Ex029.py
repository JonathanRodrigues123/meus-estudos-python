# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

vel = float(input('Quantos km/h seu carro percorreu?: '))

if vel > 80 :
    multa = (vel - 80) * 7
    print(f'Você ultrapassou o limite de velocidade, o valor da sua multa é de R${multa:.2f}')
else:
    print('Prossiga, dirija com cuidado, tenha um ótimo dia!')
