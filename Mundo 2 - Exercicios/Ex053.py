# Crie um programa que leia uma frase qualque e diga se ela é um palindromo, desconsiderando os espaços.


# Ex: APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O BOLO / ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase que deseja: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Por tanto, é um palíndromo.')
else:
    print('Por tanto, não é um palíndromo.')
#====================================================

