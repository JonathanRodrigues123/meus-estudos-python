# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.


print('Gerador de PA')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ',end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos deseja mostrar?: '))
print(f'Fim do programa com {total} de termos mostrados')
