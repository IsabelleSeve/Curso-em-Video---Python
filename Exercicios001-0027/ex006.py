# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n*2
t = n*3
rq = n**(1/2)
print('O número digitado foi {}. \nSeu dobro é {}. \nSeu triplo é {}.'.format(n,d,t))
print('Por fim, sua raiz quadrada é {:.2f}'.format(rq))