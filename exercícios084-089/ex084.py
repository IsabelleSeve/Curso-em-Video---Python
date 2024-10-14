# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as mais leves.

pessoas = []
cadastros = []
cont = 0
resp = "S"
leves = []
pesadas = []

while resp == "S":
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    cadastros.append(nome)
    cadastros.append(peso)
    pessoas.append(cadastros)

    if peso <= 70:
        leves.append(nome)
    else:
        pesadas.append(nome)

    cont += 1
    resp = input('Deseja continuar[S/N]: ').upper()

print("Pessoas cadastradas:")
for pessoa in pessoas:
    print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]}')

print(f'Foram cadastradas: {cont} pessoas')

if leves:
    print('As pessoas mais leves são:')
    for leve in leves:
        print(leve)
else:
    print('Não há pessoas leves cadastradas.')

if pesadas:
    print('As pessoas mais pesadas são:')
    for pesada in pesadas:
        print(pesada)
else:
    print('Não há pessoas pesadas cadastradas.')

#Olhar cód do notion