# Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuário
# O programa será interrompido quando o numero solicitado for negativo.


print('TABUADA')

while True:
    n = int(input('Digite um numero para saber a sua tabuada: '))
    if n < 0:
        break
    for t in range(1, 10):
        print(f'{n} x {t} = {n*t}')
print('Tabuada finalizada!')