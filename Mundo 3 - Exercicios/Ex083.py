# Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.


expres = str(input('Digite uma expressão (com parênteses): '))
pilha = []
for simb in expres:
    if simb == '(':
        pilha.append('(')
    if simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')