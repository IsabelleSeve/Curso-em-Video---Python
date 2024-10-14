#Crie um programa que vai ler váris números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valoores pares e ímpares digitads, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
lista = []
pares = []
impares = []
resp = "s".upper()
while resp == "S":
    valores = int(input("Digite um número inteiro: "))
    lista.append(valores)
    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)
    resp = str(input("Deseja continuar [s/n]? ")).upper()
print(f'Os números digitados foram: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')