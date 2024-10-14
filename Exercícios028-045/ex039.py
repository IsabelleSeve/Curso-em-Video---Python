#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de alistar.
# Se já passou do tempo do alistamento.
# O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('Esse é um programa para avaliar seu estado com relação ao alistamento militar')
sexo = str(input("Digite seu sexo por favor, 'F' para mulher e 'M' para homem: "))
dtn = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - dtn
velho = idade - 18
novo = 18 - idade
if sexo == "F":
    print("Você é mulher e não precisa fazer parte do alistamento obrigatório")
elif sexo == "M" and idade > 18:
    print("Quem nasceu em {} atualmente tem {} anos e já passou {} anos do tempo do alistamento militar.".format(dtn, idade, velho))
elif sexo == "M" and idade < 18:
    print("Quem nasceu em {} atualmente tem {} anos e falta {} anos para o alistamento militar.".format(dtn, idade, novo))
elif sexo == "M" and idade != 18:
    print("Quem nasceu em {} tem {} anos e está pronto para o alistamento militar neste momento!".format(dtn, idade))

