# Criando comandos personalizados:

def lin():
    print('-'*30)
# programa principal
lin()
print('CURSO EM VIDEO')
lin()
print('APRENDA PYTHON')
lin()
print('GUSTAVO GUANABARA')
lin()
#===============================================
# criando comando personalizados usando parametros:

def mensagem(msg):
    print('-------------------------------')
    print(msg)
    print('-------------------------------')

# programa principal
mensagem('SISTEMA DE ALUNOS')

# criando função:

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

# programa principal
titulo('CURSO EM VIDEO')
titulo('PYTHON É MUITO BOM!')
titulo('OI')
