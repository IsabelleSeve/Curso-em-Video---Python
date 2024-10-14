# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário/ 2 para octal/ 3 para hexadecimal
print('Olá eu sou um programa de conversão')
num = int(input('Primeiro digite um número inteiro: '))
print('-' * 5, 'Conversões', '-' * 5)
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
# Para facilitar a vida eu poderia ter colocado 3 aspas dentro do print e ir pulando linha da forma que eu quisesse
es = int(input('Escolha uma das três opções para converter o número: '))
if es == 1:
    print('{} convertido para Binário é {}'.format(num, bin(num)[2:]))
elif es == 2:
    print('{} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif es == 3:
    print('{} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Por favor, escolha apenas alguma das opções anteriores.')
