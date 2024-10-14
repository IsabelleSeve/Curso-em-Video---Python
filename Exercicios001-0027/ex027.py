# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#ex: Ana Maria de Souza
#primeiro: Ana
#segundo: Souza
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Primeiro Nome: {}'.format(nome[0]))
print('O último nome é: {}'.format(nome[len(nome)-1]))
