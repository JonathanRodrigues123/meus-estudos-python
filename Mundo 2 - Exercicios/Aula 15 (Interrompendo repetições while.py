# Exemplos:


'''cont = 1
while cont <= 10:
    print(cont, '...',end='')
    cont += 1
print('Acabou')'''

#======================================================================
'''n = soma = 0
while n != 999:
    n = int(input('Digite um numero: '))
    soma += n
print(f'A soma vale {soma}')'''
#=====================================
n = soma = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
print(f'A soma vale {soma}')