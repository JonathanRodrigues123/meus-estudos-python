# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. Pergunte o valor
# da casa , o salário do comprador e em quantos anos ele vai pagar.

# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa?: R$'))
salario = float(input('Quanto você receber?: R$'))
anos = int(input('Quantos anos você deseja pagar a prestação?: '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar um casa de R${casa:.2f} em {anos} anos')
print(f'A prestação será de {prestacao:.2f}')


if prestacao <= minimo:
    print('Emprestimo sera CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')