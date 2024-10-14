# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
# que é a condição de parada. No final mostre quantos números foram digitados e qual a soma entre eles.
# desconsiderando o flag.

cont = 0
soma = 0
num = 0
while num != 999:
    cont += 1
    num = int(input("Digite um númer inteiro, use '999' para parar o programa: "))
    soma += num
print("Você digitou {} números.".format(cont-1))
print("A soma entre eles é: {}".format(soma - 999))