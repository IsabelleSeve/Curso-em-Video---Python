# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
n = float(input('digite um número real: '))
print('sua parte inteira é: {}'.format(n.__int__()))