# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
a = randint(0,4)
b = randint(0,4)
c = randint(0,4)
d = randint(0,4)
e = randint(0,4)
tupla = a,b,c,d,e
ordem = sorted(tupla)
print(f'Os números sorteados foram: {tupla}')
print(f'O menor número é {ordem[0]} e o menor é {ordem[4]}')


