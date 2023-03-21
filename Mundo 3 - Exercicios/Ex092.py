# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.


from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: ')).title()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Possui carteira de trabalho? [0 para não possui]: '))
if dados['CTPS'] != 0:
    num = 12345678910
    num_limitado = round(num)
    if dados['CTPS'] == num_limitado:
        dados['contratação'] = int(input('Ano de contratação: '))
        dados['salário'] = float(input('Salário: R$'))
        dados['aposentadoria'] = dados['idade'] + (dados['contratação'] +35) - datetime.now().year
    while dados['CTPS'] != num_limitado:
        print('CTPS inválido!')
        break

print(dados)
