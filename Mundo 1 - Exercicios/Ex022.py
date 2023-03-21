# Crie um programa que leia o nome completo de uma pessoa e mostre:


# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.



nome = str(input('Seu nome completo: ')).strip()
separa = nome.split
print(f'Seu nome em maiúsculas {nome.upper()}')
print(f'Seu nome em minúsculas {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))