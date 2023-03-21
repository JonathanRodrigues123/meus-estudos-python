# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto


preço = float(input('Digite o preço atual: R$'))
desconto = preço - (preço * 5 / 100)
print(f'O preço atual do produto custa R$ {preço:.2f}, com 5% de desconto vai custar R$ {desconto:.2f}')