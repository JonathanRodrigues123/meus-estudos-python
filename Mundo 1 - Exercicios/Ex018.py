# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do sêno, cosseno e tangente desse ângulo.

# OBS os valores seno, cosseno e tangente, não estão em graus sentigrados eles devem estar em radianos, para isso 
# deve importar o comando (radians).

import math
angulo = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo {angulo} tem o SENO {seno:.2f}')
coss = math.cos(math.radians(angulo))
print(f'O ângulo {angulo} tem o COSSENO {coss:.2f}')
tan = math.tan(math.radians(angulo))
print(f'O ângulo {angulo} tem a TANGENTE {tan:.2f}')