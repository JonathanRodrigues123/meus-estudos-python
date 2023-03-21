# Variaveis compostas

'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'Eu vou comer {comida} pra caramba!')'''

#==============================================================

'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')'''

#==============================================================
'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')'''
#===============================================================
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(sorted(lanche)) # sorted = organizar(colocar em ordem)
print(lanche)
#===============================================================
'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # a + b = faz a junção das tuplas''' 
#print(c)
#print(len(c)) # len(c) = mostra o tamanho da tupla
#print(c.cont(5))# c.cont(?) = mostra quantas vezes o elemento selecionado aparecem no programa
#print(c.index(8)) # index(?) = mostra em que posição as tuplas selecionada estão
#print(c.index(5, 1))# c.index(5, 1) = faz um deslocamento do elemento selecionado'''
#================================================================
'''pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)# del = apagar da memoria (OBS: Não é possivel deletar apenas um iten)
print(pessoa)'''