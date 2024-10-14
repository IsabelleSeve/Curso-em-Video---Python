# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
from time import sleep
print('Vamos ver se eu sou um pouco esperta?')
print('Vamos fazer assim, você vai digitar um número e eu vou dizer se ele é ímpar ou par')
num = int(input('Já pensou em um número? Então me diga qual é: '))
print('Processanso...')
sleep(2)
if num%2==0:
    print('Esse é um número par.')
else:
    print('Esse é um número ímpar.')
