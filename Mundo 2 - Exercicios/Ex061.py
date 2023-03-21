# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,mostrandoos 10 primeiros termos da progressão 
# usando a estrutura while.

print('Gerador de PA')

primeiro = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
    
print('Fim')