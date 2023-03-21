# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.


r1 = float(input('Primeir seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes seguimentos podem formar um triângulo.')
else:
    print('Estes seguimentos não podem formar um triângulo.')
