# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores e ímpares, em ordem crescente.

lista = []
par = []
impar = []
for programa in range(0,7):
    valores = int(input('Digite um valor inteiro: '))
    lista.append(valores)
    if valores % 2 == 0:
        par.append(valores)
    else:
        impar.append(valores)
par.sort()
impar.sort()
print(f'Os números digitados foram: {lista}')
print(f'Os números pares são: {par}')
print(f'Os números ímpares são? {impar}')


#fiz errado, é uma única lista
#Olhar cód do notion