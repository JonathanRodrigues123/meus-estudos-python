num = [2, 5, 9, 1]
num[2] = 3 
num.append(7)# -> adiciona um valor ao elemento
num.sort()# -> coloca os valores em ordem crescente
num.sort(reverse=True)# -> coloca os valores em ordem decrescente
num.insert(2, 2)# -> o mesmo que inserir(adicionar valores) em uma lista
num.pop(2) # -> remove numeros opcionais da lista
if 2 in num:
    num.remove(2)# -> remove um numero opcional da lista
else:
    print('numero 5 não encontrado')
print(num)
print(f'Essa lista tem {len(num)} elementos')

###################################################

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor: ')))

for c, v in enumerate(valores): # enumerate pega tento chave(c) quanto o valor(v) do for
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

############################################################

'''a = [2, 3, 4, 5, 7]
b = a[:] # <- cria uma copia da letra (a)
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''