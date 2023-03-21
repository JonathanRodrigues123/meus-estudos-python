# Crie um programa que leia dois valores e mostre um menu como o ao lado da tela:
# Seu programa deverá realizar a operação solicitada em cada caso.

# [ 1 ] somar  [ 2 ] multiplicar  [ 3 ] maior  [ 4 ] novos numeros  [ 5 ] sair do programa
from time import sleep
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opçao = 0
while opçao != 5:
    print('''Escolha uma operação abaixo:
    [ 1 ] somar  [ 2 ] multiplicar  [ 3 ] maior  [ 4 ] novos numeros  [ 5 ] sair do programa''')
    opçao = int(input('Escolha uma opção de calculo: '))

    if opçao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opçao == 2:
        multi = n1 * n2
        print(f'{n1} x {n2} = {multi}')
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior é {maior}')
    elif opçao == 4:
        print('Escolha dois valores para calcular: ')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    elif opçao == 5:
        print('Finalizando...')
    sleep(2)
print('Programa finalizado com sucesso!')
