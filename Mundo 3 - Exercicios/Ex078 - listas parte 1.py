# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

#===========================================================
num = []
maior = menor = 0
for c in range(0, 5):
        num.append(str(input(f'Digite o {c} valor: ')))
        if c == 0:
                maior = menor = num[c]
        else:
                if num[c] > maior:
                        maior = num[c]
                elif num[c] < menor:
                        menor = num[c]

print(f'Os valores digitados na lista foram: {num}')
print(f'O maior valor da lista foi: {maior} nas posições: ',end='')
for i, v in enumerate(num):
        if v == maior:
                print(f'{i}...',end='')
print()
print(f'O menor valor da lista foi: {menor} nas posições: ',end='')
for i, v in enumerate(num):
        if v == menor:
                print(f'{i}...',end='')
print()

