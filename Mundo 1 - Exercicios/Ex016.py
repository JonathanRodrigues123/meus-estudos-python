# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tabela a sua porção inteira
# Ex: Digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6

from math import trunc
num = float(input('Digite um valor: '))
print(f'O numero digitado foi {num} e a sua porção inteira é {trunc(num)}')
#-----------------------------------------------------------------------------------
'''num = float(input('Digite um valor: '))
inteiro = int(num)
print(f'O numero digitado foi {num} e a sua porção inteira é {inteiro}')'''