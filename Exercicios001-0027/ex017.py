# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
co = int(input('Digite a medida do cateto oposto do triângulo: '))
ca = int(input('Digite a medida do cateto adjacente do triângulo: '))
hi= (co**2+ca**2)**(1/2)
print('A hipotenusa será: {}'.format(hi))