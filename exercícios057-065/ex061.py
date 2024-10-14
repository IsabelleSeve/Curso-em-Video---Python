#Refaça o desafio 051, lendo o primiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print("="*20)
print("10 Termos de uma PA")
print("="*20)
pt = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1

while cont <= 10:
    pa = pt + (cont - 1) * razao # ao invés de usar essa expressão, poderia ter usado apenas termo += razao
    cont += 1
    print("{}".format(pa), end=" → ")
print("Fim")