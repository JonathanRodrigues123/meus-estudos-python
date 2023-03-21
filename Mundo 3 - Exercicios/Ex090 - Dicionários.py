# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).strip().title()
aluno['media'] = float(input('Média: '))
if aluno['media'] == 6.5:
    aluno['situação'] = 'RECUPERAÇÃO'
if aluno['media'] <= 6:
    aluno['situação'] = 'REPROVADO'
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'

for k, v in aluno.items():
    print(f'{k}: {v}')

    
'''nome = str(input('Nome: ')).title()
media = float(input(f'A média de {nome}: '))
ficha = {"nome": nome, "media": media}
for k, v in ficha.items():
    print(f'A situação de {k} é igual a {v}')
if media == 6.5:
    print(f'Situação é igual a recuperação!')
if media <= 6:
    print(f'Situação é igual a reprovado!')
if media >= 7:
    print(f'Situação é igual aprovado!')'''