# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores. (maioridade = 21 anos)
from datetime import date
contmais = 0
contmenos = 0
atual = date.today().year
for c in range(0,7):
    nasc = int(input("Digite seu ano de nascimento:"))
    if atual - nasc < 21:
        contmenos += 1
    else:
        contmais += 1
print("{} pessoas atingiram a maioridade".format(contmais))
print("{} ainda não atingiram a maioridade".format(contmenos))