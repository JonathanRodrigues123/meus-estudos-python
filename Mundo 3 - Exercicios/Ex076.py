# Crie um programa que tenha uma tupla única com nomes de produtos e seu respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Biscoito', 1.99, 'Guaraná', 5.99, 'Nescal', 6.59, 'Sabão', 0.69, 'Detergente', 2.99)

print('PROMOÇÕES DE NATAL, SÓ PREÇOS BAIXOS:')
print('-'*37)
for pos in range(len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:5}')