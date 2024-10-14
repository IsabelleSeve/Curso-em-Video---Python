# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
cont = 1
import random
from time import sleep
print('Primeiro eu vou pensar em um número entre 0 e 10')
sleep(1.5)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
print('Pronto, pensei.')
n1 = random.randint(0,10) #faz o computador ¨pensar¨
n2 = int(input("Agora é sua vez, tente adivinhar o número em que pensei: "))
while n2 != n1:
    cont += 1
    n2 = int(input("Errou! Tente novamente: "))
print("Você precisou de {} tentativas para acertar o número que eu estava pensando .".format(cont))