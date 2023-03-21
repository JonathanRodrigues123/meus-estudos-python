# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele
# ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento:  '))

idade = atual - ano
print(f'Quem nasceu em {ano}, tem {idade} anos de idade.')

if idade == 18:
    print('Você deve se alistar neste ano, o quanto antes!')
elif idade < 18:
    saldo = 18 - idade
    total = atual + saldo
    print(f'Você ainda não completou 18 anos, faltam {saldo} anos para alistar-se.')
    print(f'Seu alistamento será no ano de {total}.')
elif idade > 18:
    saldo = idade - 18
    total = atual - saldo
    print('Você ja passou do prazo do seu alistamento!')
    print(f'Você deveria ter se alistado a {saldo} anos atrás.')
    print(f'Seu alistamento foi no ano de {total}')
    
