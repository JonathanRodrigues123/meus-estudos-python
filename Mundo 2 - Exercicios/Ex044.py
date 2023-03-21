# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros


preço = float(input('Preço do produto: R$'))
print('''Forma de pagamento: 
[ 1 ] À vista dinheiro/cheque com 10% de desconto
[ 2 ] À vista no cartão com 5% de desconto
[ 3 ] 2x no cartão no preço normal
[ 4 ] 3x ou mais no cartão com 20% de juros''')
opçao = int(input('Escolha sua forma de pagamento: '))

if opçao == 1:
    desconto = preço - (preço * 10 / 100)
    print(f'Sua compra à vista em dinheiro, vai custar R${desconto:.2f} no final')
elif opçao == 2:
    desconto = preço - (preço * 5 / 100)
    print(f'Sua compra à vista no cartão, vai custar R${desconto:.2f} no final')
elif opçao == 3:
    parcela = preço / 2
    print(f'Sua compra será parcelado em 2x de R${parcela:.2f} no preço normal no final')
elif opçao == 4:
    juros = preço + (preço * 20 / 100)
    parcela = int(input('Quantas vezes no cartão você vai parcelar?: '))
    totparcela = juros / parcela
    print(f'Sua compra será parcelado em {parcela}x de  R${totparcela:.2f} com 20% de juros')
else:
    juros = preço
    print('Opção de pagamento inválida, tente novamente')
print(f'Sua compra de R${preço:.2f} vai custar  R${juros:.2f} no final')
