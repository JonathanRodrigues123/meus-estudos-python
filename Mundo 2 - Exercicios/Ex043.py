# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, Calcule seu IMC e mostre seu status
# de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade 
# Acima de 40: Obesidade mórbida


peso = float(input('Peso [KG]'))
altura = float(input('Altura [m]'))
imc = peso / (altura ** 2)

print('Calculando o imc')

print(f'Sua massa corporal é de: {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal.')
elif 25 <= imc <= 30:
    print('Você está em obesidade.')
else:
    print('Você está em obesidade mórbida.')
