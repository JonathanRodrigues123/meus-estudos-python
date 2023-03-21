# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    maior = n1
    print('\033[30mO primeiro valor é maior')
elif n2 > n1:
    maior = n2
    print('\033[30mO segundo valor é maior')
else:
    print('\033[31mNão existe valor maior, os dois são iguais')
