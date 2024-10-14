# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse Ângulo
import math
from math import sin,cos,tan
a = float(input('Digite o valor de um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno de {} é {:.2f},\nO cosseno é {:.2f}\nE a tangente é {:.2f}'.format(a,s,c,t))
