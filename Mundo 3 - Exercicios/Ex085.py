# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre - os em uma única lista que
# mantenha separados os valores pares e impares. No final, mostre os valores em ordem crescente.

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}ª valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Os valores pares da lista foram: {num[0]}')
print(f'Os valores impares da lista foram: {num[1]}')
