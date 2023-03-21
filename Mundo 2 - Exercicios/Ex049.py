# Refaça o DESAFIO 009,mostrando a tabuada de um numero que o usuário escolher.
# Só que agora utilizando um laço for.

num = int(input('Digite um numero para saber sua tabuáda: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c}')
