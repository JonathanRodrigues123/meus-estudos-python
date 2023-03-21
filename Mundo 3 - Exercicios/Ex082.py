# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Os valores adicionados na lista: {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
print(f'Os valores pares da lista: {pares}')
for i, v in enumerate(lista):
    if v % 2 == 1:
        impares.append(v)
print(f'Os valores impares da lista: {impares}')
