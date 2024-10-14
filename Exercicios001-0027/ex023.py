#faça um programa que leia um número do 0 a 9999 e mostre na tela cada um dos digitos separados.
# ex: digite um número: 1834
# unidade: 4
# dezena: 3
# centena:8
#milhar: 1

num = int(input('Digite um número de 0 a 9999: '))
n =str(num)
print('Unidade:{}'.format(n[3]))
print('Dezena:{}'.format(n[2]))
print('Centena:{}'.format(n[1]))
print('Milhar:{}'.format(n[0]))