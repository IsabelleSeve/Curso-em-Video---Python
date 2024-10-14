# faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
print('Vamos descobrir se o ano é bissexto? Coloque 0 para analisar o ano atual:')
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é de fato um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
