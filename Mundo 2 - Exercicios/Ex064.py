# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros 

# formam digitados e qual foi a soma entre eles(desconsiderando o flag).


soma = cont = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]: '))
print(f'A soma dos {cont} valores é igual a {soma}')