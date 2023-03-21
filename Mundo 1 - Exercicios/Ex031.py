# Desenvolva um programa que pergunte a distancia de uma viagem em km.Calcule o preço da passagem
# cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem?: '))
print(f'Você está preste a começar uma viagem de {distancia}Km')
if distancia <= 200:
        preço = distancia * 0.50
        print(f'O valor da passagem será de R${preço:.2f}')

elif distancia > 200:
        preço = distancia * 0.45
        print(f'O valor da passagem seá de R${preço:.2f}')
