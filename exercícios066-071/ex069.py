# Crie um programa que leia a idade e o sexo de várias pessoas, A cada pessoa cadastrada o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram
# cadastrados. C) quantas mulheres tem menos de 20 anos.
contdezo = 0
homens = 0
mulheres = 0
print("-"*10, "Pesquisa", "-"*10)
while True:
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [F/M]: ")).upper().strip()[0]
    resp = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    print("-"*30)
    if idade > 18:
        contdezo += 1
    if sexo == "F":
        if idade < 20:
            mulheres += 1
    else:
        homens += 1
    if resp == "N" or resp != "S":
        break
print("-"*10, "Resultados", "-"*10)
print(f"{contdezo} pessoas tem mais de 18 anos")
print(f"{homens} homens foram cadastrados")
print(f"{mulheres} mulheres tem menos de 20 anos")



