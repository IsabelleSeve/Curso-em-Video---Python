# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
import pygame
pygame.init() #para iniciar o pygame
pygame.mixer.music.load('ex021.mp3') #para selecionar o arquivo
pygame.mixer.music.play() #para tocar
input() #na versão atual precisa desse inputx
pygame.event.wait()
