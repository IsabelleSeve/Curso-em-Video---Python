# O professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele
# lendo o nome deles e escrevendo o nome escolhido
import random
a1 = str(input('Digite o nome de um dos alunos '))
a2 = str(input('Digite o nome de outro aluno '))
a3 = str(input('Digite o nome de outro aluno '))
a4 = str(input('Digite o nome de outro aluno '))
r = random.SystemRandom(a1,a2,a3,a4)
print('O escolhido para apagar o quadro foi: {}'.format(r))

#correção:
import random
b1 = str(input('Primeiro aluno: '))
b2 = str(input('Segundo aluno: '))
b3 = str(input('Terceiro aluno: '))
b4 = str(input('Quarto aluno: '))
lista = [b1,b2,b3,b4]
escolhido = random.choice(lista)
print('O escolhido para apagar a lousa foi {}'.format(escolhido))