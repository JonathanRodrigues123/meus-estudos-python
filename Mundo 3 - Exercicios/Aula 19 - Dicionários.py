#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#del pessoas['sexo'] # deleta um item da lista
#pessoas['nome'] = 'Leandro' # Troca um item da lista para a qual você escolheu.
#pessoas['peso'] = 98.5 # adiciona um elemento na lista
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
'''for k in pessoas.keys():
    print(k)'''
'''for k in pessoas.values():
    print(k)'''
'''for k, v in pessoas.items():
    print(f'{k} = {v}')'''
#------------------------------------------------------------------------------------
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
#print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

'''filme = {"TITULO":'STAR WARS', "ANO":'1977',"DIRETOR":'JORGE LUCAS'}
filme['TITULO'] = 'MATRIX'

for k, v in filme.items():
    print(f'O {k} é {v}')'''


