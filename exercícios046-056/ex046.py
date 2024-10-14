# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji
import pygame
for c in range(2,0,-1):
    print(c)
    sleep(1)
print(emoji.emojize("""Boom! :collision: :collision: :collision:
:collision::collision:
:collision::collision::collision:""")) #:collinion:
pygame.init()
pygame.mixer.music.load('fogos de artíficios.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


#ver como faz para o barulho repetir várias vezes