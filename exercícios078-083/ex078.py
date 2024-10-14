#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista =  [int(input("Digite um valor inteiro: ",)),
         int(input("Digite um valor inteiro: ",)),
         int(input("Digite um valor inteiro: ",)),
         int(input("Digite um valor inteiro: ",)),
         int(input("Digite um valor inteiro: ",))]
print("=+="*10)
print(f'Os números digitados foram: {lista}')
novalista = lista[:]
lista.sort()
novalista[:] == lista[4]
print(f'O maior valor digitado foi {lista[4]}. Na posição {novalista.index(lista[4]) + 1 }!')
print(f'O menor valor digitado foi {lista[0]}. Na posição {novalista.index(lista[0]) + 1 }!')


#dificuldade em encontrar a maior posição