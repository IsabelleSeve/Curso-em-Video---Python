# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# sequência Fibonacci.
# Ex: 0 - 1 -1 - 2 - 3 - 5 - 8
print("-"*34)
print("-"*5, "Sequência de Fibonacci","-"*5)
print("-"*34)
termos = int(input("Quantos termos deseja apresentar: "))
t1 = 0
t2 = 1
cont = 3
print("-"*34)
print("{} → {} ".format(t1,t2), end="")
while cont <= termos:
    t3 = t1 + t2
    print("→ {} ".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print(" → Fim")