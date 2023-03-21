# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos,
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Primeiro aluno: ')).title()
a2 = str(input('Segundo aluno: ')).title()
a3 = str(input('Terceiro aluno: ')).title()
a4 = str(input('Quarto aluno: ')).title()

lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação do trabalho será {lista}')