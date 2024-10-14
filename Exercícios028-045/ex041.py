# A Confederação Nacional  de Natação precisa de um programa que leia o ano de nscimento de um atleta e mostre sua
# categoria, de acordo com a idade:
#Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master
from datetime import date
print("Olá somos da Confederação Nacional de Natação e precisamos saber em qual categoria você se encaixa para "
      "participar para a competição.")
nascimento = int(input("Digite em que ano você nasceu: "))
ano = date.today().year
idade = ano - nascimento
if idade <= 9 :
      print("Você tem {} anos e se encaixa na categoria Mirim".format(idade))
elif idade <= 14 :
      print("Você tem {} anos e se encaixa na categoria Infantil".format(idade))
elif idade <= 19:
      print("Você tem {} anos e se encaixa na categoria Junior".format(idade))
elif idade <= 20:
      print("Você tem {} anos e se encaixa na categoria Sênior".format(idade))
else:
      print("Você tem {} anos e se encaixa na categoria Mastee".format(idade))



