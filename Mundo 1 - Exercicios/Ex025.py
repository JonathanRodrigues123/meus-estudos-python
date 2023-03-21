# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.


nome = str(input('Digite um nome:')).strip().title()
v = 'Silva' in nome
print('Seu nome tem Silva?')
print(f'Resposta: {v}')