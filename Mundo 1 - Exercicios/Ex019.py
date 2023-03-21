# Um professor que sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
a1 = str(input('Primeiro aluno: ')).title()
a2 = str(input('Segundo aluno: ')).title()
a3 = str(input('Terceiro aluno: ')).title()
a4 = str(input('Quarto aluno: ')).title()
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'O aluno sorteado para apagar o quadro foi {escolhido}')