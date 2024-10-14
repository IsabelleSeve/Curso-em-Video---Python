# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo


print('Vamos testar uma coisa?')
print('Você vai digitar 3 medidas e eu vou analisar se é possível construir um triângulo com essas medidas ')
n1 = int(input('Digite a primeira medida: '))
n2 = int(input('Digite a segunda medida: '))
n3 = int(input('Digite a terceira medida: '))
if (n1+n2)>n3 and (n2+n3)>n1 and (n1+n3)>n2:
    print('Com essas medidas é possível construir um triângulo')
else:
    print('Com essas medidas não é possível construir um triângulo, sinto muito, teve novamente')