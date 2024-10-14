# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidero-o.
s = 0
print("Vamos fazer continhas? \nDigite 6 valores inteiros e eu somarei apenas os números pares. ")
for c in range(0,6):
    n = int(input("Digite um número inteiro: "))
    if n%2==0:
        s += n
print("A soma dos números pares digitados é: {}".format(s))

#outra resolução:
#soma = 0
#cont = 0
#for c in range(1, 7):
#   num = int(input("Digite um {} valr: ".format(c)))d
#   if num % 2 == 0:
#       soma += num
#       cont += 1