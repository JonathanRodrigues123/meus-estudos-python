# Crie um programa onde o usuário possa digitar vários valores numéricos 
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele
# não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente

lista = []
while True:
    num = int(input('Digite um valor desejado: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado na lista')
    else:
        print('Valores replicados não são aceitos!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer adicionar mais um numero  [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
print(f'Os valores digitados em ordem crescente são: {lista} ')


















