# Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre a sua média.


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = n1 + n2 / 2
print(f'A primeira nota foi {n1}, a segunda nota foi {n2} e a media das duas notas foi {media:.1f}')