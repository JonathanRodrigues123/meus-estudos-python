# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles 
# que forem pares. Se o valor digitado for impar, desconsidere-o.


soma = cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}ª valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma dos {cont} valores pares é igual a {soma}')