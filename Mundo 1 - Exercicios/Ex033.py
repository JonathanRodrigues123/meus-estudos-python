# Faça um programa que leia um três numeros e mostre qual é o maior e qual é o menor.

from re import A


a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

maior = a # ja considerei que (a) é maior
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
menor = a # ja considerei que (a) é menor
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

print(f'O maior valor foi {maior} e o menor valor foi {menor}')


