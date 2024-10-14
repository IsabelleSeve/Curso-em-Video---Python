# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado peça a digitação
# novamente até ter um valor correto.

boot = "S"
while boot == "S":
    boot = str(input("Deseja participar do pesquisa [S/N]? ")).upper()
    if boot == "S":
        sexo = str(input("Digite seu sexo [F/M]: ")).upper()
        if sexo != "F" and sexo != "M":
            print("Erro! \nDigite apenas alguma das opções acima!")
print("Sexo {} registrado. Muito obrigada!".format(sexo))


# professor
#sex = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]   o strip serve para ignorar os espaços escritos errads
# e o upeer()[0] serve para deixar tudo maipusculo e mesmo que a pessoa digite masculino/ feminino, eele vai reconhecer
#while sexo not in 'MmFf':
#   sexo = str(input('Dads inválidos. Por favor informe seu sexo')).strip().upper()[0]
#print('Sexo registrado com sucesso.')