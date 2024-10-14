# Faça um programa que leia um número qualquer e mostre seu fatorial.
# tentar com for e com while

#formas de fazer:
#from math import factorial
#n = int(input("Digite um número para calcular seu fatorial: "))
#f = factorial(n)
#print("O fatorial de {} é {}".format(n, f))

#Jeito usando o laço while:
n = int(input("Digite um número e calcularemos seu fatorial: "))
c = n
f = 1
print("Calculando  {}! = ".format(n), end="")
while c>0:
    print("{}".format(c), end="")
    print(" x " if c>1 else " = ", end = "")
    f *= c
    c -= 1
print("{}".format(f))
print
#Desafio: Fazer o exercício usando o laço for
num = int(input("Digite um número e calcularemos seu fatorial: "))
cont = num
fa = 1
for fat in range(num,0,-1):
    print(fat," x " if fat>1 else " = ", end="")
    fa *= fat
    cont -= 1
    print("{}".format(fa))

    # perguntar pro metre theo