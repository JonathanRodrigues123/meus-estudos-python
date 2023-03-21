# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
# de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


from time import sleep
print('\033[32mContagem regressiva para o ano novo!')
for c in range(10, -1, -1):
    print(f'{c}')
    sleep(1)
print('\033[31mBOOOM!')
sleep(1)
print(' '*2)
print('\033[31mBOOOM')
sleep(1)
print(' '*2)
print('\033[31mPOOOOW!')
