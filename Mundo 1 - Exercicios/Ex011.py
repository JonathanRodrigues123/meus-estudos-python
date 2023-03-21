# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintar-a,

# sabendo que cada litro  de tinta, pinta uma área de 2m²

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = (larg * alt)


print(f'A largura da parede tem {larg}x{alt}, e sua area é de {area}m² ')
tinta = area / 2
print(f'Para pinta essa parede é necessário {tinta}L de tinta')
