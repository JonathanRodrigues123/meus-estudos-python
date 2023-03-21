# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o ultimo nome separadamente.

# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza



nome = str(input('Nome completo: ')).title().strip().split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O ultimo nome é: {}'.format(nome[-1]))