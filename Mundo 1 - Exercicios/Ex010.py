# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar.

# Considere US$ 1,00 = R$5,31

real = float(input('Quanto dinheiro você tem?: R$'))

dolar = real / 5.31 #considerado o valor do dolar do ano de 2021
print(f'Com R$ {real:.2f} você pode comprar RS${dolar:.2f} ')