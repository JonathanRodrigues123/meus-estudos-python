# Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o 
# usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram 

# digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = cont = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} é igual a {soma}')