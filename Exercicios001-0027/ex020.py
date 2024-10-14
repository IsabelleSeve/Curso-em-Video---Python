# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
a1 = str(input('Digite o nome de um dos alunos '))
a2 = str(input('Digite o nome de outro aluno '))
a3 = str(input('Digite o nome de outro aluno '))
a4 = str(input('Digite o nome de outro aluno '))
lista = [a1,a2,a3,a4]
random.shuffle(lista) #shuffler serve para embaralhae
print('A ordem de apresentação do trabalho é: {}'. format(lista))

#aprimorando código
from random import shuffle
a1 = str(input('Digite o nome de um dos alunos '))
a2 = str(input('Digite o nome de outro aluno '))
a3 = str(input('Digite o nome de outro aluno '))
a4 = str(input('Digite o nome de outro aluno '))
lista = [a1,a2,a3,a4]
shuffle(lista) #shuffler serve para embaralhae
print('A ordem de apresentação do trabalho é: {}'. format(lista))