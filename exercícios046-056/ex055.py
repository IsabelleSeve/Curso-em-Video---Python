# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior peso lido e qual foi o menor.
maior = 0
menor = 0
for p in range(0,5):
    peso = float(input("Digite seu peso por favor: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso inserido na pesquisa foi: {:.2f}Kg".format(maior))
print("O menor peso inserido na pesquisa foi: {:.2f}Kg".format(menor))