# Crie um programa que simule o funcionamnto de um caixa eletrônico. No inicio,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues. 

# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('CAIXA ELETRÔNICO')

saldo = int(input('digite o valor das cédulas que deseja sacar:'))
total = saldo
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R${ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
