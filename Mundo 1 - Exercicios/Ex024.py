# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.


cid = str(input('Nome de uma cidade: ')).strip()
print(cid[:5].title() == 'Santo')

