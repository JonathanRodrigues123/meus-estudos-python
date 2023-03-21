# Faça um programa que leia uma frase pelo teclado e mostre:


# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip().lower()

print('A frase {} tem {} letras A'.format(frase, frase.count('a')))
print('A frase {} aparece a primeira letra A na posição {}'.format(frase, frase.find('a') + 1))
print('A frase {} aparece a ultima letra A na posição {}'.format(frase, frase.rfind('a') + 1))