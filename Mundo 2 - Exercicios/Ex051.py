# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('Termos da PA')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, (decimo + razao), razao):
    print(f'{c} -> ',end=' ')
print('Fim')
