# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas 
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = menor = 0
for pess in range(1, 8):
    nasc = int(input(f'Que ano a {pess}° pessoa nasceu?: '))

    idade = atual - nasc

    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1

print(f'Temos ao todo {maior} pessoa maiores de idade cadastradas.')
print(f'E {menor} pessoas menores de idade cadastradas')