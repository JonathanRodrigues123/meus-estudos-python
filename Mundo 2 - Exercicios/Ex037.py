# Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão:

# 1 para binário / 2 para octal / 3 para hexadecimal

num = int(input('Digite um numero: '))
print('''Escolha uma das bases de conversão:
[ 1 ] binário  [ 2 ] octal  [ 3 ] hexadecimal''')

opcao = int(input('Escolha sua conversão: '))

if opcao == 1:
    print(f'O numero é {num} e a convesão para binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O numero é {num} e a conversão para octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O numero é {num} e a conversão para hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente!')
