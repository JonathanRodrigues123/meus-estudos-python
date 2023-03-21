# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.


soma = media = quant = maior = menor = 0
resp = 'S'
while resp in 'S':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / quant
print(f'A media de todos os {quant} valores é {media:.2f}')
print(f'O maior numero lido foi {maior}')
print(f'O menor numero lido foi {menor}')