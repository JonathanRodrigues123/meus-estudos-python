# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os numeros pares.


num = (int(input('Digite um numero: ')),
    int(input('Digite o proximo numero: ')),
    int(input('Digite o proximo numero: ')),
    int(input('Digite o ultimo numero: ')))

print('Os numeros digitados foram: ',end='')
for n in num:
    print(f'{n}',end=' ')
       
print(f'\nO numero 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 foi digitado na {num.index(3)+1}ª posição')
else:
    print('Numero 3 não encontrado!')
print('Os numeros Pares encontrados são: ',end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
    