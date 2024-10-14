# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:  A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
total = 0
maismil = 0
barato = 0
nomebarato = ""
cont = 0
print("="*30)
print("{:-^30}".format(" Seu Toba "))
print("="*30)
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: R$"))
    resp = str(input("Deseja continuar cadastrando mais produtos [S/N]: ")).upper().strip()[0]
    barato = preco
    total += preco
    cont += 1
    if resp == "S":
        if preco > 1000:
            maismil += 1
        if cont == 1 or preco < barato:
            barato = preco
            nomebarato = nome
    if resp != "SN" :
        resp = str(input('respostas válidas [S/N]. '
                         'Deseja continuar?'))
    else: 
            break
print("="*30)
print("{:-^30}".format("Analisando"))
print("="*30)
print(f"O valor total da compra é R${total:.2f}.")
print(f"{maismil} protudos custam mais de R$1000,00.")
print(f"{nomebarato} é o produto mais barato.")