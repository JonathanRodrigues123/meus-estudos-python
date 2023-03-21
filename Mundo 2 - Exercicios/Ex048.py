# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c

print(f'A soma dos {cont} valores é igual a {soma}')