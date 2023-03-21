# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informaçôes
# possiveis sobre ela.


print('Tratando métodos')

nome = input('Nome: ')

print('O tipo primitivo do nome é:', type(nome))
print('Seu nome esta em maiúsculas?: ',nome.isupper())
print('Seu nome esta em minúsculas?: ',nome.islower())
print('Seu nome esta capitalizado?: ',nome.istitle())
print('Seu nome é um numeral?: ',nome.isnumeric())
print('Seu nome é um alfanumerico?: ',nome.isalnum())
print('Seu nome é um alfabeto?: ',nome.isalpha())
print('Só tem espaços?:',nome.isspace())