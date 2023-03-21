# Crie um programa que vai ler vários números e colocar em uma lista,
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    l = len(lista)
    lista.sort(reverse=True)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista tem {l} valores')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('Valor 5 foi adicionado na lista!')
else:
    print('Valor 5 não encontrado!')