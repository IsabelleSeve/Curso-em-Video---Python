# escreva um programa que leia dois números inteiros e compare-os,  mostrando na tela uma mensagem:
# O primeiro valor é maior / O segundo valor é maior / Não existe valor maior, os dois são iguais
print('Vamos comparar dois números?')
n1 = int(input('Escreva um número inteiro: '))
n2 = int(input('Escreva outro número inteiro: '))
if n1 > n2:
    print('O primeiro valor, {}, é maior.'.format(n1))
elif n2 > n1:
    print('O segundo valor, {}, é maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais.')
