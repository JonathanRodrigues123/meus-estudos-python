# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250.00,calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Quanto o funcionário recebe?: R$'))

if salario <= 1.250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} com aumento passou a receber R${novo:.2f}')
