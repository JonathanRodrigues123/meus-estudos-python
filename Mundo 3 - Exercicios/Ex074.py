# Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior
# valor que estão na tupla.

from random import randint

numeros = randint(1, 10), randint(1, 10), randint(1, 10),randint(1, 10),randint(1, 10)

for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior numero foi {max(numeros)}')
print(f'O menor numero foi {min(numeros)}')