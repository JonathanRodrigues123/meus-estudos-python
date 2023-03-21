# Listas

# exemplo de lista

#  Pessoas:
#  ----------------------------------------
# |['Pedro', 25 |'Maria', 19 | 'João', 32] |
# |    0      1 | 0       1  |    0     1  |
#  ----------------------------------------
#         0           1           2

# print(pessoas[0][0]) =  Pedro
# print(pessoas[1][1]) =  19
# print(pessoas[2][0]) = João
# print(pessoas[1]) = ['Maria', 19]

'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:]) # [:] = CRIA - SE UMA COPIA DAS ESTRUTURAS 
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
#=========================================================================
'''galera = [['João', 19], ['Maria', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
#==========================================================================
galera = list()
dados = list()
pmaior = pmenor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')).strip().title())
    dados.append((int(input('Idade: '))))
    galera.append(dados[:])
    dados.clear()
#print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'Temos {p[0]} é maior de idade.')
        pmaior += 1
    else:
        print(f'Temos {p[0]} é menor de idade.')
        pmenor += 1
print(f'Temos {pmaior} maior de idade e {pmenor} menor de idade')

