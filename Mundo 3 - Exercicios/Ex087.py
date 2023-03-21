# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
somap = somav = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l}, {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    print()
print(f'A soma dos valores pares da matriz é: {somap}')
for l in range(0, 3):
    somav += matriz[l][2]
print(f'A soma dos valores da terceira coluna da matriz é: {somav}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f'O maior valor da segunda linha da matriz é: {mai}')
