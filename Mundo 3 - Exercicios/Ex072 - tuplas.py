# Crie um programa que tenha uma tupla totalmente preenchida por extenso, de zero até vinte,
# Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('\033[mDigite um numero entre 0 e 20: '))
    while num not in range(0, 21):
        num = int(input('\033[mNumero inválido, digite um numero entre 0 e 20: '))
    print(f'\033[32mVocê digitou o numero {cont[num]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[mQuer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[32mPrograma finalizado!')




'''numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinse', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
for c in range(len(numeros)):
    num = int(input('Digite um numero entre 0 e 20: '))
    
    if 0 <= num <= 20:
        break
    print('Tente novamente!' ,end='')
print('Você digitou o numero - ',end='')
print(numeros[num])'''

