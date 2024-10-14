# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²,
al = float(input('Digite a altura da parede em metros: '))
la = float(input('Digite a largura da parede em metros: '))
ar = al*la
ti = ar/2
print('A área da parede é {}m³, e serão necessário {}L de tinta'.format(ar,ti))