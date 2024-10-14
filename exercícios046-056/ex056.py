# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# - A média de idade do grupo.- Qual o nome do homem mais velho. - Quantas mulheres têm menos de 20 anos.
maiorh = 0
media = 0
mnome = ''
cont = 0
print("Somos do IBGE e precisamos fazer uma pesquisa rápida!")
for c in range(1,5):
    print("{:->5} Entrevista".format(c), "-"*4)
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite qual o seu sexo, sendo 'F' para feminino e 'M' para masculino: "))
    media += idade

    if sexo == "M" and idade > maiorh :
        maiorh = idade
        mnome = nome
    if sexo == "F" and idade < 20:
        cont += 1
print("-"*5,"Resultado","-"*5)
print("Mulher(es) com menos de 20 anos: {}". format(cont))
print("O nome do homem mais velho é: {}".format(mnome))
print("A média da idade do grupo é: {}".format(media / 4))
