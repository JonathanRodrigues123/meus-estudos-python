# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:


# Equilátero: todos os lados iguais
# Isosceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 or r3 < r1 + r2:
    print('Estes seguimento FORMAM UM TRIÂNGULO ',end='')

    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    elif r1 == r2 != r3 and r2 == r1 != r3 or r3 == r1 != r2 or r3 == r2 != r1:
        print('ISOSCELES')
else:
    print('Os seguimentos digitados NÃO PODEM FORMAR UM TRIÂNGULO')