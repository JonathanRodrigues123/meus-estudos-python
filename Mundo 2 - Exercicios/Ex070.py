# Crie um programa que leia nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar. No final mostre:

# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000.
# Qual é o nome do produto mais barato.
total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    preco = int(input('Preco: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total de compras foi R${total:.2f}')
print(f'Foram comprados {totmil} produtos com valor maior que R$1000,00')
print(f'O produto mais barato da sua compra foi: {barato} no valor R${menor:.2f}')