# Faça um programa que leia um número inteiro e morte na tela se sucessor e antecessor.
n = int(input('Digite um número inteiro: '))
s = n+1
a = n-1
print('O número digitado é {}, seu antecessor é {} e seu sucessor é {}'.format(n,a,s))
# Outra forma de resolver é:
# n = int(input('Digite um número: '))
# print('Analisando o valor {}, seu sucessor é {} e o antecessor é {}'.format(n,n-1,n+1))
