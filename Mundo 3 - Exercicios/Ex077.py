# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Carro', 'Copo', 'python', 'curso', 'aulas', 'casa', 'sonhar', 'televisão',
            'caminhão', 'presidente', 'xupeta')

for p in palavras:
    print(f'\nna palavra {p.upper()} temos as vogais: ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra.lower()}',end=' ')