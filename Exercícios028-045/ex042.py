#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero
# Isosceles ok
# Escaleno ok

print('Vamos testar uma coisa?')
print('Você vai digitar 3 medidas e eu vou analisar se é possível construir um triângulo com essas medidas ')
n1 = int(input('Digite a primeira medida: '))
n2 = int(input('Digite a segunda medida: '))
n3 = int(input('Digite a terceira medida: '))
if n1+n2>n3 and n2+n3>n1 and n1+n3>n2:
    print('Com essas medidas é possível construir um triângulo!')
    if ((n1 == n2) and (n1 != n3)) or ((n2 == n3) and (n2 != n1)) or ((n3 == n1) and (n1 != n2)):
        print('Ele será um triângulo Isósceles.')
    if n1 != n2 != n3 != n1:
        print('Ele será um triângulo Escaleno.')
    if n1 == n2 == n3:
        print('Ele será um triângulo Equilátero.')

else:
    print('Com essas medidas não é possível construir um triângulo, sinto muito, teve novamente')