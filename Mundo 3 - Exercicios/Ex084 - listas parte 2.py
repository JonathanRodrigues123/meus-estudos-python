# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')).title())
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas {len(dados)} pessoas na lista.')
print()
print(f'O maior peso da lista foi {mai}Kg / Pesos de: ',end='')
for p in dados:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso da lista foi {men}kg / Pesos de: ',end='')
for p in dados:
    if p[1] == men:
        print(f'[{p[0]}] ',end='')
#====================================================

