# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de pessoas do grupo.
# Qual é o nome do homen mais velho.
# Quantas mulheres tem menos de 20 anos.

somaidade = mediaidade = maioridadevelho = mulhermenor20 = 0
nomevelho = ''

for p in range(1, 5):
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadevelho:
        maioridadevelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenor20 += 1

mediaidade = somaidade / 4
print(f'\033[36mA idade media de pessoas do grupo é {mediaidade} anos')
print(f'O homen mais velho do grupo tem {maioridadevelho} anos, e se chama {nomevelho}')
print(f'Temos ao todo {mulhermenor20} pessoa do sexo feminino menor de 20 anos')