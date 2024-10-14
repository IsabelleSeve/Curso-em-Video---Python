# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores lidos  qual foi o maior e o menor valores lidos. O programa deve perguntar a usuário se ele quer
# ou não continuar a digitar valores.
cont = 0
resp = "S"
soma = 0
media = 0
maior = 0
menor = 0
print("Sou um programa para calcular a média dos valores inseridos.")
while resp == "S":
    resp = str(input("Deseja participar do programa [S/N]? ")).upper().strip()[0]
    if resp == "S":
        num = int(input("Digite um número: "))
        cont += 1
        soma += num
        media = soma/cont
        if cont == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    else:
        print("Obrigata!")

print("A média dos valores lidos é: {}".format(media))
print("O maior valor lido foi {} e o menor {}".format(maior, menor))
