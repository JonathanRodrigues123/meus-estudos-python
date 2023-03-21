# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
# salário, com 15% de aumento.


salario = float(input('Qual é o seu salário?: R$ '))
novo = salario + (salario * 15 / 100)
print(f'O funcionario que recebia R$ {salario:.2f}, com 15% de aumento passou a receber R$ {novo:.2f}')