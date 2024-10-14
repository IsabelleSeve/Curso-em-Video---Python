# Faça um programa que leia um número inteito e diga se ele é ou não um número primo.
num = int(input("Digite um número inteiro e iremos verificar se ele é primo: "))
s = 0
# for primo in range(1,num):
#    s += 1
#    if num % s == 0:
#    print("número primo")
#       else:
#           print("Não é número primo")
for c in range(1, num +1):
    if num % c ==0:
        print("\033[33m", end="")
        s += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(c), end="")
print("\n\033[mO número {} foi divisível {} vezes". format(num, s))
if s == 2:
    print("Portanto é um número primo".format(c))
else:
    print("Ele não é um número primo".format(c))
