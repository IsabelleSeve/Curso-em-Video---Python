#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
v = int(input('Escreva um valor em metros: '))
cm = v*100
mm = cm*10
print('Metros: {}m'.format(v))
print('Centímentros {}cm'.format(cm))
print('Milímetros: {}mm'.format(mm))