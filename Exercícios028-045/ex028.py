# Escreva um programa que faça o computador ¨pensar¨ em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random   #o professor usou from random import randint para facilitar
from time import sleep
print('Primeiro eu vou pensar em um número entre 0 e 5')
sleep(2)
print('................................................')
sleep(2)
print('Pronto, pensei.')
n1 = int(input('Agora tente adivinhar o número: '))
n2 = random.randint(0,5) #faz o computador ¨pensar¨
print('processando...')
sleep(3)
if n1==n2:
    print('Você é demais, acertou!')
else:
    print('Sinto muito, não foi dessa vez, eu tinha pensado no número {}'.format(n2))
