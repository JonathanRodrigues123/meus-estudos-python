# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 1:
        
        print(f'\033[36m',end=' ') 
        tot += 1    
    else:
        print(f'\033[m',end=' ')
    print(f'{c}',end=' ')
print(f'\n\033[mO numero {num} é divisivel {tot} vezes.')

if tot == 2:
    print('Por tanto, é um numero PRIMO.')
else:
    print('Por tanto, não é um numero PRIMO.')
