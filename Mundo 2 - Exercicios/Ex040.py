# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando um mensagem no final,
# de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO 
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota do aluno: '))

nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2

print('Resultado de notas')
print(f'A primeira nota foi {nota1} e a segunda nota foi {nota2} a média foi {media:.1f}')
if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO!')
elif media >= 7.0:
    print('APROVADO!')
