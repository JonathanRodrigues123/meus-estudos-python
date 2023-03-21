# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média. 

pessoas = dict()
galera = list()
media = soma = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).title()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO: Por favor digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar fazendo cadastro? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO: Por favor digite apenas S ou N.')
    if resp == 'N':
        break
print(f'A) Foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'B) A média de idade do grupo cadastrado é: {media:.2f} ')
print('C) As pessoas do sexo feminino cadastradas foram: ',end=' _ ')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}',end=' _ ')
print()
print('As pessoas com idade acima da média do grupo cadastrado foram: ',end='')
for p in galera:
    if p['idade'] >= media:
        print('    ',end='')
        for k, v in pessoas.items():
            print(f'{k} = {v}',end=' ')


        
