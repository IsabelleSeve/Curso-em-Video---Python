# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com toda as letras minúsculas
# Quantas letras ao todo tem, sem considerar espaços
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
dividido = nome.split()
print('Analisando seu nome................')
print('Seu nome primeiro nome é...{}'.format(dividido[0]))
print('Seu nome com todas as letras em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format((nome.lower())))
print('Seu nome tem {} letras ao todo'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {}'.format(len(dividido[0])))