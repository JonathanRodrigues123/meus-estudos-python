# Escreva um programa que leia um valor em metros e a axiba convertido
# em centimetros e milimetros.

medida = float(input('Digite um valor: '))

cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm')

