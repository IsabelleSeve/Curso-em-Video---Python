# Crie um programa que faça o computador jogar jokenpô com você
#import random
#from time import sleep
#print('Vamos jogar jokenpô?')
#print('As opções são:\n[1] Pedra \n[2] Papel \n[3] Tesoura')
#pedra = 'Pedra'
#papel = 'Papel'
#stesoura = 'Tesoura'
#lista = [pedra, papel, tesoura]
#escomp = random.choice(lista)
#es = input('Escolha uma das três opções: ')
#sleep(0.01)
#print('Eu escolhi {}'.format(escomp))
#if (es == 1 and escomp == pedra) or (es == 2 and escomp == papel) or (es == 3 and escomp == tesoura):
#    print('Empatamos hehe, pura sorte sua!')
#elif (es == 1 and escomp == papel) or (es == 2 and escomp == tesoura) or (es == 2 and escomp == pedra):
#    print('Eu ganhei, seu merda!!')
#elif (es == 1 and escomp == tesoura) or (es == 2 and escomp == pedra) or (es == 3 and escomp == papel):
#    print('Você ganhou, mas isso nem é grande coisa assim.')
#else:
#    print("Alguma coisa deu errado, tente de novo!")

#Forma como o professor fez:
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print("Vamos jogar jokenpô?? Dúvido você ganhar de mim!")
jogador = int(input("Suas opções são: \n[0]Pedra\n[1]Papel\n[2]Tesoura\nQual você escolhe?  "))
print("Eu joguei {}".format(itens[computador]))
print("E você jogou {}".format(itens[jogador]))
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print("Empatamos hehe, pura sorte sua!")
    elif jogador == 1:
        print("Você ganhou, mas isso nem é grande coisa assim.")
    elif jogador == 2:
        print("Eu ganhei, seu merda!!")
    else:
        print("Jogada inválida!")
elif computador == 1:   #computador jogou papel
    if jogador == 0:
        print("Eu ganhei, seu merda!!")
    elif jogador == 1:
        print("Empatamos hehe, pura sorte sua!")
    elif jogador == 2:
        print("Você ganhou, mas isso nem é grande coisa assim.")
    else:
        print("Jogada inválida!")
elif computador == 2:   #computador jogou tesoura
    if jogador == 0:
        print("Você ganhou, mas isso nem é grande coisa assim.")
    elif jogador == 1:
        print("Eu ganhei, seu merda!!")
    elif jogador == 2:
        print("Empatamos hehe, pura sorte sua!")
    else:
        print("Jogada inválida!")