# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = 0
for pess in range(1, 6):
    peso = float(input(f'Peso da {pess}° pessoa: [KG]'))
    if pess == 1: # para cada pessoa que o programa identificar.
        maior = menor = peso # maior e menor é igual a peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:      
            menor = peso
print(f'O maior peso lido foi {maior}Kg e o menor peso lido foi {menor}Kg')